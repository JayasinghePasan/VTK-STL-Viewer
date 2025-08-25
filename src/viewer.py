import vtk
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PySide6 import QtWidgets

class VTKWidget( QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QtWidgets.QVBoxLayout()
        self.vtk_widget = QVTKRenderWindowInteractor(self)
        layout.addWidget(self.vtk_widget)
        self.setLayout(layout)

        self.renderer = vtk.vtkRenderer()
        self.vtk_widget.GetRenderWindow().AddRenderer(self.renderer)
        self.iren = self.vtk_widget.GetRenderWindow().GetInteractor()

        self.actor = None
        self.renderer.SetBackground(0.1, 0.1, 0.1)

        self.iren.Initialize()

    def load_stl(self, filename: str):
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        if self.actor:
            self.renderer.RemoveActor(self.actor)

        self.actor = vtk.vtkActor()
        self.actor.SetMapper(mapper)
        self.actor.GetProperty().SetColor(0.9, 0.8, 0.3)

        self.renderer.AddActor(self.actor)
        self.renderer.ResetCamera()
        self.vtk_widget.GetRenderWindow().Render()
        