import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QListWidget, QTextEdit, QLabel, QHBoxLayout
)
from PySide6.QtCore import Qt, QThread, Signal
from services.scanning_service import ScanningService
from services.validation_service import ValidationService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Validation Tool")
        self.resize(800, 600)
        self.scanned_objects = []
        self.validation_results = {}

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
        for obj in self.scanned_objects:
            self.object_list.addItem(obj.name)

    def run_validations(self):
        validation_service = ValidationService()
        self.validation_results = validation_service.validate_objects(self.scanned_objects)
        self.update_object_list_status()

    def update_object_list_status(self):
        for index in range(self.object_list.count()):
            item = self.object_list.item(index)
            obj = self.scanned_objects[index]
            obj_results = self.validation_results.get(obj, [])
            worst_status = self.get_worst_status(obj_results)
            item.setForeground(self.get_color_for_status(worst_status))

    def get_worst_status(self, results):
        status_order = {
            'ERROR': 3,
            'WARNING': 2,
            'GOOD': 1
        }
        worst = 'GOOD'
        for _, result in results:
            if status_order[result.status.name] > status_order[worst]:
                worst = result.status.name
        return worst

    def get_color_for_status(self, status):
        colors = {
            'GOOD': Qt.green,
            'WARNING': Qt.yellow,
            'ERROR': Qt.red
        }
        return colors.get(status, Qt.black)

    def display_validations(self, item):
        index = self.object_list.row(item)
        obj = self.scanned_objects[index]
        obj_results = self.validation_results.get(obj, [])
        text = f"Validations for {obj.name}:\n"
        for validator, result in obj_results:
            text += f"- {validator.__class__.__name__}: {result.status.name}\n"
            text += f"  {result.message}\n"
        self.validation_text.setText(text)
