#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2

class MyVideoCapture():
    DELAY=100 # 100 msecのディレイ

    def __init__(self):
        # PCによってはカメラID=0ではなく1を指定するとうまくいく
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def run(self):
        while(True):
            # カメラ画像を１枚キャプチャする
            ret, frame = self.cap.read()

            # リターンコードが0でなければ終了
            if not ret:
                break

            # キャプチャしたカメラ画像を加工
            img = np.copy(frame) # 加工するともとの画像が保存できないのでコピーを生成
            # 画像の中心を示すターゲットマークを描画
            # rows, cols, channels = img.shape
            # img = cv2.circle(img, (int(cols/2), int(rows/2)), 30, (0, 0, 255), 3)
            # img = cv2.circle(img, (int(cols/2), int(rows/2)), 60, (0, 0, 255), 3)
            # img = cv2.line(img, (int(cols/2), int(rows/2) - 80), (int(cols/2), int(rows/2) + 80), (0, 0, 255), 3)
            # img = cv2.line(img, (int(cols/2) - 80, int(rows/2)), (int(cols/2) + 80, int(rows/2)), (0, 0, 255), 3)

            # 左右反転（顔を撮るときは左右反転しておくとよい, 0: 上下反転, 1: 左右反転, -1: 左右上下反転）
            img = cv2.flip(img, flipCode=1)

            # 加工した画像を表示
            cv2.imshow('frame', img)

            # 次の画像を処理するまでに時間間隔（msec）を空ける
            # キーボードのqが押されたら終了
            if cv2.waitKey(self.DELAY) & 0xFF == ord('q'):
                self.captuered_img = frame
                break

    def get_img(self) -> cv2.Mat:
        """キャプチャ画像を取得
        """
        return self.captuered_img

    def write_img(self):
        """キャプチャ画像をファイルに保存
        """
        cv2.imwrite('camera_capture.png', self.captuered_img)

    def __del__(self):
        # 終了処理
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = MyVideoCapture()
    app.run()
    app.write_img()