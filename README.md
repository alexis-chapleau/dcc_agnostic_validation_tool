


# DCC-Agnostic Validation Tool
Welcome to the DCC-Agnostic Validation Tool! This tool is designed to perform scene validations in various Digital Content Creation (DCC) applications like Autodesk Maya, SideFX Houdini, Blender, and others, using a unified, extensible, and scalable architecture.

# Key goals of the tool:

DCC-Agnostic: Works across multiple DCC applications with minimal changes.
Extensible: Easily add new validations, models, and support for additional DCCs.
Maintainable: Clean architecture adhering to SOLID principles.
Testable: Comprehensive unit tests and mock implementations for testing outside DCC environments.
Features
Unified Interface: Consistent user interface across different DCCs.
Modular Architecture: Decoupled components for scanning, validation, and UI.
Extensible Validations: Easily add new validators for different object types.
DCC Integration Layer: Abstracts DCC-specific code into dedicated classes.
Standalone Mode: Run and test the tool outside of DCC applications using mocked data.
Testing Framework: Unit tests with mock adapters to simulate DCC environments.
Architecture Overview
High-Level Architecture
The tool follows a layered architecture:

UI Layer: Provides the graphical user interface using PySide6.
Service Layer: Contains business logic for scanning and validation.
Domain Layer: Defines models representing scene objects.
DCC Integration Layer: Abstracts DCC-specific functionality.
Adapter Layer: Interfaces with DCC APIs via adapters.
Utils Layer: Utility classes and functions.

# Getting Started
Prerequisites
Python 3.7+
PySide6 (Qt for Python)
DCC Applications (e.g., Autodesk Maya 2025, Blender) for running inside a DCC
Git (for cloning the repository)
Installation
Clone the Repository

    git clone https://github.com/yourusername/dcc_agnostic_validation_tool.git
    cd dcc_agnostic_validation_tool
Create a Virtual Environment

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies


    pip install -r requirements.txt
If requirements.txt is not provided, manually install necessary packages:


    pip install PySide6
Running the Tool
Standalone Mode
You can run the tool outside of any DCC application using mocked data.


    python main.py
The tool will launch with a GUI populated with mocked scene objects.
You can perform validations as if running inside a DCC.
Inside a DCC (e.g., Maya)
To run the tool inside Autodesk Maya:

Open Maya's Script Editor

Go to Windows > General Editors > Script Editor.    
Paste the Launch Script


    import sys
    import os
    import importlib

# Add your project directory to sys.path
    project_path = 'Your_Package_Location/dcc_agnostic_validation_tool'
    if project_path not in sys.path:
        sys.path.insert(0, project_path)

# Import and run the main function
    try:
        import main
        importlib.reload(main)
        main.main()
    except Exception as e:
        import traceback
        traceback.print_exc()
Adjust project_path to your project location.
Execute the Script

Select all the code in the Script Editor.   
Press Ctrl + Enter (Windows) or Cmd + Enter (macOS).    
The tool will launch within Maya, using real scene data.      
Testing
Unit Tests
The project includes unit tests to ensure code quality and functionality.

Install Testing Dependencies

    pip install pytest pytest-qt
    Run Tests


    pytest tests/
# Testing the UI
UI tests are included to test the GUI components using pytest-qt.

Tests are located in the tests/ directory.
Mock services are used to simulate DCC environments.
# Extending the Tool
## Adding a New Validation
Adding a new validation involves creating a new validator class and updating the ValidatorFactory.

Example: Implementing a Polycount Validator
Step 1: Create a New Validator Class

Create a new file polycount_validator.py in the validators/ directory.


# validators/polycount_validator.py

    from validators.base_validator import BaseValidator
    from utils.validation_result import ValidationResult, ValidationStatus

    class PolycountValidator(BaseValidator):
        def execute(self):
            # Assume obj has a method get_polycount()
            polycount = self.obj.get_polycount()
            max_polycount = 10000  # Define maximum allowed polycount

            if polycount > max_polycount:
                return ValidationResult(
                    status=ValidationStatus.ERROR,
                    message=f"Polycount ({polycount}) exceeds the maximum allowed ({max_polycount})."
                )
            else:
                return ValidationResult(
                    status=ValidationStatus.GOOD,
                    message="Polycount is within the acceptable range."
                )


## Step 2: Update the Validator Factory

Modify ValidatorFactory to include the new validator.

## validators/validator_factory.py

    from validators.name_validator import NameValidator
    from validators.polycount_validator import PolycountValidator
    from models.mesh import Mesh
    
    class ValidatorFactory:
        @staticmethod
        def get_validators(obj):
            validators = [NameValidator(obj)]
            if isinstance(obj, Mesh):
                validators.append(PolycountValidator(obj))
            return validators

# Step 3: Implement get_polycount Method in the Mesh Model

Ensure that your Mesh model has a get_polycount method.


## models/mesh.py
    
    from models.scene_object import SceneObject
    
    class Mesh(SceneObject):
        def get_polycount(self):
            # Implement logic to get polycount from the DCC
            # This could use the API adapter pattern
            return self.api_adapter.get_polycount(self)
Adding Support for a New DCC    
To add support for a new DCC application, implement a new subclass of DCCApplication and update the DCCFactory.

Example: Implementing Blender Integration   
Step 1: Implement BlenderApplication Class  

Create blender_application.py in the dcc/ directory.


# dcc/blender_application.py
    
    from dcc.dcc_application import DCCApplication
    from typing import Optional
    from PySide6.QtWidgets import QWidget
    import bpy
    
    class BlenderApplication(DCCApplication):
        def get_main_window(self) -> Optional[QWidget]:
            # Blender does not use Qt for its UI, so this may be None or custom
            return None  # Alternatively, implement a way to embed the UI in Blender
    
        def is_standalone(self) -> bool:
            return False
Step 2: Update DCCDetector

Modify DCCDetector to detect Blender.


# utils/dcc_detector.py
    
    import os
    
    class DCCDetector:
        @staticmethod
        def get_current_dcc():
            if 'MAYA_LOCATION' in os.environ:
                return 'maya'
            elif 'BLENDER_USER_SCRIPTS' in os.environ:
                return 'blender'
            else:
                try:
                    import maya.cmds
                    return 'maya'
                except ImportError:
                    pass
                try:
                    import bpy
                    return 'blender'
                except ImportError:
                    pass
                return 'standalone'
Step 3: Update DCCFactory

Add Blender support to DCCFactory.  

# dcc/dcc_factory.py
    
    from dcc.blender_application import BlenderApplication
    
    class DCCFactory:
        @staticmethod
        def get_dcc_application() -> DCCApplication:
            dcc = DCCDetector.get_current_dcc()
            if dcc == 'maya':
                return MayaApplication()
            elif dcc == 'blender':
                return BlenderApplication()
            else:
                return StandaloneApplication()
Step 4: Implement DCC-Specific API Adapters

Create API adapters and scanners for Blender.

# adapters/blender_api_adapter.py
    
    from adapters.api_adapter import ApiAdapter
    
    class BlenderApiAdapter(ApiAdapter):
        def get_scene_objects(self):
            # Use Blender's API to get scene objects
            import bpy
            objects = []
            for obj in bpy.data.objects:
                # Convert Blender objects to your SceneObject models
                # ...
                pass
        return objects
Step 5: Implement Scanners for Blender

Create scanners that use the Blender API adapter.


# services/scanners/mesh_scanner.py

    from services.scanners.base_scanner import BaseScanner
    from models.mesh import Mesh
    
    class MeshScanner(BaseScanner):
        def scan(self):
            # Use the API adapter to get meshes
            scene_objects = self.api_adapter.get_scene_objects()
            meshes = [Mesh(obj.name) for obj in scene_objects if obj.type == 'MESH']
            return meshes
Adding a New Model
Adding a new model involves creating a new class in the models/ directory.

Example: Implementing a Light Model
Step 1: Create the Light Model

Create light.py in the models/ directory.


# models/light.py

    from models.scene_object import SceneObject
    
    class Light(SceneObject):
        def __init__(self, name):
            super().__init__(name)
            # Add any light-specific properties
            self.intensity = None
            self.color = None
    
        def get_intensity(self):
            # Implement logic to get intensity from the DCC
            return self.api_adapter.get_light_intensity(self)
    
        def get_color(self):
            # Implement logic to get color from the DCC
            return self.api_adapter.get_light_color(self)
Step 2: Update Scanners to Include Lights

Modify or create a scanner to find lights in the scene.


# services/scanners/light_scanner.py
    
    from services.scanners.base_scanner import BaseScanner
    from models.light import Light
    
    class LightScanner(BaseScanner):
        def scan(self):
            # Use the API adapter to get lights
            scene_objects = self.api_adapter.get_scene_objects()
            lights = [Light(obj.name) for obj in scene_objects if obj.type == 'LIGHT']
            return lights
Step 3: Update ScanningService

Include the LightScanner in the scanning process.


# services/scanning_service.py
    
    from services.scanners.scanner_factory import ScannerFactory
    
    class ScanningService:
        @staticmethod
        def scan_scene():
            scanners = ScannerFactory.get_scanners()
            all_objects = []
            for scanner in scanners:
                all_objects.extend(scanner.scan())
            return all_objects
    Update ScannerFactory to include LightScanner:


# services/scanners/scanner_factory.py
    
    from services.scanners.camera_scanner import CameraScanner
    from services.scanners.mesh_scanner import MeshScanner
    from services.scanners.light_scanner import LightScanner
    
    class ScannerFactory:
        @staticmethod
        def get_scanners():
            api_adapter = ApiAdapterFactory.get_api_adapter()
            return [
                CameraScanner(api_adapter),
                MeshScanner(api_adapter),
                LightScanner(api_adapter),
            ]
Step 4: Implement Validations for Lights

Optionally, create validators for the new Light model.  

Implementing New Features   
To implement new functionalities:   

Identify the Layer  

Determine where the new feature fits in the architecture (UI, service, domain, etc.).
Follow Existing Patterns    

Implement new classes following the structure and patterns of existing classes.
Update Dependencies 

Adjust factories and services to include the new functionality.
Write Tests 

Ensure that new code is covered by unit tests.
# Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository

Create a personal fork on GitHub.
Create a Feature Branch


    git checkout -b feature/new-feature
Commit Changes

    git commit -am 'Add new feature'
Push to Your Fork


    git push origin feature/new-feature
Submit a Pull Request

Open a pull request on GitHub with a description of your changes.   
# License
This project is licensed under the MIT License. See the LICENSE file for details.

Thank you for using the DCC-Agnostic Validation Tool! If you have any questions or need assistance, feel free to reach out.