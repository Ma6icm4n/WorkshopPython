import sys

if r"C:\Users\Asus\Desktop\WorkshopPython\lib" not in sys.path:
    sys.path.append(r'C:\Users\Asus\Desktop\WorkshopPython\lib')
    sys.path.append(r'C:\Users\Asus\Desktop\WorkshopPython\pipeline')

from Qt import QtWidgets, QtCompat
from pipeline.ui import my_window as mw

app = QtWidgets.QApplication(sys.argv)

win = mw.MyWindow()
win.show()

sys.exit(app.exec_())