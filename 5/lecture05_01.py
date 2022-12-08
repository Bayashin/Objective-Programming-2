#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http.cookiejar import MozillaCookieJar
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PySide6 import QtGui, QtCore
from my_module.K21099.lecture05_sample import GameModel

class MainWidget(QWidget):
    def __init__(self, game_model : GameModel):
        super().__init__()
        self.game_model = game_model
        self.mark = game_model.get_mark()
        self.top_label = QLabel()
        self.top_label.setText("ゲームメッセージ")
        self.top_label.setFont(QtGui.QFont('Arial', 20))
        self.top_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.buttons = [QPushButton() for _ in range(9)]
        [btn.setFont(QtGui.QFont('Arial', 40)) for btn in self.buttons]
        #[btn.clicked.connect(self.__click) for btn in self.buttons]
        self.buttons[0].clicked.connect(self.__click_0_0)
        self.buttons[1].clicked.connect(self.__click_0_1)
        self.buttons[2].clicked.connect(self.__click_0_2)
        self.buttons[3].clicked.connect(self.__click_1_0)
        self.buttons[4].clicked.connect(self.__click_1_1)
        self.buttons[5].clicked.connect(self.__click_1_2)
        self.buttons[6].clicked.connect(self.__click_2_0)
        self.buttons[7].clicked.connect(self.__click_2_1)
        self.buttons[8].clicked.connect(self.__click_2_2)
        layout1 = QGridLayout()
        layout1.addWidget(self.top_label,0,0)
        layout2 = QGridLayout()
        for i in range(3):
            for j in range(3):
                layout2.addWidget(self.buttons[i*3+j], i, j)
        layout3 = QGridLayout()
        self.update_btn = QPushButton()
        self.update_btn.setText("更新")
        self.update_btn.setFont(QtGui.QFont('Arial', 20))
        self.update_btn.clicked.connect(self.__show_game_state)
        layout3.addWidget(self.update_btn, 0,0)
        layouts = QGridLayout()
        layouts.addLayout(layout1, 0,0)
        layouts.addLayout(layout2, 1,0)
        layouts.addLayout(layout3, 2,0)
        self.setLayout(layouts)

        self.__show_game_state()

    def __show_game_state(self):
        print(self.game_model.get_game_state())
        game_state = self.game_model.get_game_state()
        array = game_state[0] + game_state[1] + game_state[2]
        [btn.setText("" if state==0 else "○" if state==1 else "x") for btn, state in zip(self.buttons,array)]

    def __click_0_0(self):
        print(0)
        self.__btn_event(0)

    def __click_0_1(self):
        print(1)
        self.__btn_event(1)

    def __click_0_2(self):
        print(2)
        self.__btn_event(2)

    def __click_1_0(self):
        print(3)
        self.__btn_event(3)

    def __click_1_1(self):
        print(4)
        self.__btn_event(4)

    def __click_1_2(self):
        print(5)
        self.__btn_event(5)

    def __click_2_0(self):
        print(6)
        self.__btn_event(6)

    def __click_2_1(self):
        print(7)
        self.__btn_event(7)

    def __click_2_2(self):
        print(8)
        self.__btn_event(8)

    def __btn_event(self, btn_index):
        col = int(btn_index/3)
        row = btn_index%3
        message = self.game_model.update(col, row, self.mark)
        self.mark = 3 - self.mark
        self.__show_game_state()
        self.top_label.setText(message)

if __name__ == "__main__":
    game_model = GameModel()
    # game_model.update(1,1,1)
    app = QApplication(sys.argv)
    mw = MainWidget(game_model)
    mw.show()
    mw2 = MainWidget(game_model)
    mw2.show()
    app.exec()