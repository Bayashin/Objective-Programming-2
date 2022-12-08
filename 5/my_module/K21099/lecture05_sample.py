#!/usr/bin/env python

import sys

class GameModel():
    def __init__(self):
        self.__initialize()
    
    def __initialize(self) :
        self.state = {}
        self.state["game_state"] = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.state["next_turn"] = 1
        self.marks = [1,2] # markをViewに知らせる

    def get_mark(self):
        if len(self.marks)>0:
            return self.marks.pop(0) # marksの最初の数値を通知
        else:
            print("no mark exists")
            return None

    def get_game_state(self):
        return self.state["game_state"]

    def update(self, i, j, mark : int) -> str:
        message = "次は" + ("×" if self.state["next_turn"]==1 else "○") + "のターン"
        if self.__verify_update(i, j, mark):
            self.state["game_state"][i][j] = mark
            self.state["next_turn"] = 3 - self.state["next_turn"] # 1→2 or 2→1
            m = self.__check_win()
            if len(m)>0:
                message = m
        return message

    def __verify_update(self, i, j, mark):
        b=True
        if mark != self.state["next_turn"]:
            b=False
        if self.state["game_state"][i][j] != 0:
            b=False
        return b

    def __check_win(self) -> str:
        patterns = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        messages = [self.__check_a_line(pattern) for pattern in patterns]
        message = [m for m in messages if len(m)>0]
        if len(message)>0:
            message = message[0]
        else:
            message=""
        return message

    def __check_a_line(self, pattern : list[int]) -> str:
        line : list[int] = [self.state["game_state"][int(i/3)][i%3] for i in pattern]
        if line[0] == line[1] == line[2] == 1:
            message = "○の勝ち"
            return message
        if line[0] == line[1] == line[2] == 2:
            message = "×の勝ち"
            return message
        return ""

class GameView():
    def __init__(self, game_model : GameModel):
        self.game_model = game_model
        self.mark = None
        if self.mark is None:
            self.mark = self.game_model.get_mark()
        # もしmarkがもらえなかったら終了
        if self.mark is None:
            return
        self.start()

    def fetch_game_state(self):
        self.gamestate : list[list[int]] = self.game_model.get_game_state()

    def start(self):
        print("入力するマスの数字を入力(例: 0,0) または \"update\"を入力")
        self.fetch_game_state()
        self.print_gamestate()
        for line in sys.stdin:
            print("入力するマスの数字を入力(例: 0,0) または \"update\"を入力")
            line = line.rstrip()
            print(f"put {'○' if self.mark==1 else '×'} --> " + line)
            message = None
            if line != "update":
                message = self.update_game_state(*[int(x) for x in line.split(',')])
                self.mark = 3 - self.mark # 1人プレイモード
            self.fetch_game_state()
            self.print_gamestate()
            print(message)

    def update_game_state(self, i, j) -> str:
        return self.game_model.update(i, j, self.mark)

    def print_gamestate(self):
        for col in self.gamestate:
            s = ["." if i == 0 else "○" if i == 1 else "×" for i in col]
            print(f"{s[0]} {s[1]} {s[2]}")

    def __del__(self):
        if self.mark is not None:
            print("ゲームから抜けました")
        else:
            print("ゲームが開始できませんでした")

if __name__ == "__main__":
    model = GameModel()
    view1 = GameView(model)
    #view2 = GameView(model)
    #view3 = GameView(model)