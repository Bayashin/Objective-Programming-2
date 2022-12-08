#!/usr/bin/python

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Click me")
        self.button.clicked.connect(lambda x: print("Button Clicked, Hello!"))
        layout = QHBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

app = QApplication(sys.argv)
mw = MainWidget()
mw.show()
app.exec()