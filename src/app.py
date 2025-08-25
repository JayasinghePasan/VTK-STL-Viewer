import sys
from PySide6 import QtWidgets
from src.ui.main_window import MainWindow

class STLViewerApp:
    def __init__( self ):
        self.qt_app = QtWidgets.QApplication( sys.argv )
        self.main_window = MainWindow()

    def run( self ):
        self.main_window.show()
        sys.exit( self.qt_app.exec_())
