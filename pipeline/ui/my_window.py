import sys, os

sys.path.append(r'C:\Users\Asus\Desktop\WorkshopPython\lib')

from Qt import QtWidgets, QtCompat
from pipeline.engines import engine

ui_path = os.path.join(os.path.dirname(__file__), "my_window.ui")

class MyWindow(QtWidgets.QMainWindow):

    engine_name = engine.get_current()

    def __init__(self):
        
        super(MyWindow, self).__init__()
        QtCompat.loadUi(ui_path, self)
        self.open_button.clicked.connect(self.open)
        self.export_button.clicked.connect(self.export)

    def open(self, path):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "C:\\Users\\Asus\\Documents")
        file = self.engine_name.open(filename[0])

    def export(self):
        print('Starting Export Process')
        search_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Open Directory", "C:\\Users\\Asus\\Documents")
        self.dir_name.setText(search_dir)
        directory_out = self.dir_name.text()

        search_namespace = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\Asus\\Documents")
        self.in_namespace.setText(search_namespace[0])
        in_file = self.in_namespace.text()
        print("Extracting Namespace in " + in_file + " to " + directory_out)

        self.engine_name.export(in_file, directory_out)