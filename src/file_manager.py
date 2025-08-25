from PySide6 import QtWidgets

def load_stl_dialog(parent = None):
    options = QtWidgets.QFileDialog.Options()
    filename, _ = QtWidgets.QFileDialog.getOpenFileName( parent, "Open STL File", "", "STL File (*.stl);;AllFiles (*)", options=options)
    return filename