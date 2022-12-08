import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QHBoxLayout,QGridLayout,QVBoxLayout
from PySide6 import QtGui,QtCore

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('9x9のグリッドラベルと移動ボタン') # ウィンドウのタイトル
        self.setGeometry(100,100,200,150) # ウィンドウの位置(x,y)と大きさ(w,h)

        # 9x9のラベルを作成
        self.labels : list[QLabel] = [QLabel(str(x)) for x in range(9)]
        for label in self.labels:
            label.setFont(QtGui.QFont('Arial', 40))
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            # label.setText("○") # あとからラベルの文字を変更することも可能

        layout_grid = QGridLayout()
        # gridの行(row)と列(col)を指定してラベルを配置
        for i in range(3):
            for j in range(3):
                layout_grid.addWidget(self.labels[i*3+j], i, j)

        # 移動ボタンを作成
        self.buttons : list[QPushButton] = [QPushButton(text) for text in ["left", "top", "bottom", "right"]]
        [btn.setFont(QtGui.QFont('Arial', 40)) for btn in self.buttons]
        layout_left = QHBoxLayout()
        layout_left.addWidget(self.buttons[0])
        layout_top2bottom = QVBoxLayout()
        layout_top2bottom.addWidget(self.buttons[1])
        layout_top2bottom.addWidget(self.buttons[2])
        layout_right = QHBoxLayout()
        layout_right.addWidget(self.buttons[3])
        layout_left2right = QHBoxLayout()
        layout_left2right.addLayout(layout_left)
        layout_left2right.addLayout(layout_top2bottom)
        layout_left2right.addLayout(layout_right)

        self.layout = QVBoxLayout()
        self.layout.addLayout(layout_grid)
        self.layout.addLayout(layout_left2right)

        self.setLayout(self.layout)


app = QApplication(sys.argv)
app.setStyleSheet('QLabel{border: 1px solid black;}')
main_widget = MainWidget()
main_widget.show()
app.exec()