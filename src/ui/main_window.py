from PySide6 import QtWidgets
from PySide6.QtGui import QAction  
from src.viewer import VTKWidget
from src.file_manager import load_stl_dialog

class MainWindow( QtWidgets.QMainWindow ):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STL Viewer by PasanJ")
        self.resize(1000, 800)

        self.vtk_widget = VTKWidget()
        self.setCentralWidget(self.vtk_widget)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        open_action = QAction("Open STL", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

    def open_file(self):
        filename = load_stl_dialog()
        if filename:
            self.vtk_widget.load_stl(filename)