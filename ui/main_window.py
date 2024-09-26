import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QListWidget, QTextEdit, QLabel, QHBoxLayout, QListWidgetItem
)
from PySide6.QtCore import Qt
from services.scanning_service import ScanningService
from services.validation_service import ValidationService
from validators.validator_factory import ValidatorFactory
from utils.validation_result import ValidationStatus
from models.scene_object import SceneObject

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validation Tool")
        self.resize(800, 600)
        self.scanned_objects: List[SceneObject] = []
        self.validation_service = ValidationService()
        self.object_uuid_map = {}  # Map UUIDs to objects

        self.init_ui()
        self.scan_scene()

    def init_ui(self):
        main_layout = QHBoxLayout()

        # Object List
        self.object_list = QListWidget()
        self.object_list.itemClicked.connect(self.display_validations)
        main_layout.addWidget(self.object_list)

        # Side Panel for Validations
        self.validation_panel = QWidget()
        validation_layout = QVBoxLayout()
        self.validation_text = QTextEdit()
        self.validation_text.setReadOnly(True)
        validation_layout.addWidget(self.validation_text)
        self.validate_button = QPushButton("Validate")
        self.validate_button.clicked.connect(self.run_validations)
        validation_layout.addWidget(self.validate_button)
        self.validation_panel.setLayout(validation_layout)
        main_layout.addWidget(self.validation_panel)

        # Central Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def scan_scene(self):
        self.scanned_objects = ScanningService.scan_scene()
        self.object_list.clear()
        self.object_uuid_map.clear()
        for obj in self.scanned_objects:
            item = QListWidgetItem(obj.name)
            item.setData(Qt.UserRole, obj.uuid)
            self.object_list.addItem(item)
            self.object_uuid_map[obj.uuid] = obj

    def run_validations(self):
        self.validation_service.validate_objects(self.scanned_objects)
        self.update_object_list_status()

    def update_object_list_status(self):
        for index in range(self.object_list.count()):
            item = self.object_list.item(index)
            uuid = item.data(Qt.UserRole)
            obj_results = self.validation_service.validation_results.get(uuid, [])
            worst_status = self.get_worst_status(obj_results)
            item.setForeground(self.get_color_for_status(worst_status))

    def get_worst_status(self, results):
        status_order = {
            ValidationStatus.ERROR: 3,
            ValidationStatus.WARNING: 2,
            ValidationStatus.GOOD: 1
        }
        worst = ValidationStatus.GOOD
        for result in results:
            if status_order[result.status] > status_order[worst]:
                worst = result.status
        return worst

    def get_color_for_status(self, status):
        colors = {
            ValidationStatus.GOOD: Qt.green,
            ValidationStatus.WARNING: Qt.yellow,
            ValidationStatus.ERROR: Qt.red
        }
        return colors.get(status, Qt.black)

    def display_validations(self, item):
        uuid = item.data(Qt.UserRole)
        obj = self.object_uuid_map[uuid]
        # Get validators applicable to the object
        validator_classes = ValidatorFactory.get_validator_classes(obj)
        text = f"Validations applicable to {obj.name}:\n"
        for validator_class in validator_classes:
            text += f"- {validator_class.__name__}\n"
        # If validation results exist, display them
        if uuid in self.validation_service.validation_results:
            obj_results = self.validation_service.validation_results[uuid]
            text += "\nValidation Results:\n"
            for validator_class, result in zip(validator_classes, obj_results):
                text += f"- {validator_class.__name__}: {result.status.name}\n"
                if result.message:
                    text += f"  {result.message}\n"
        else:
            text += "\nValidations not yet executed.\n"
        self.validation_text.setText(text)
