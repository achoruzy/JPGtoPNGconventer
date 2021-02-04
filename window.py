import sys
from PySide6 import QtCore, QtWidgets, QtGui


class AppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.setWindowTitle('JPG to PNG converter')

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout_H = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.my_func)

    @QtCore.Slot()
    def my_func(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = AppWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
