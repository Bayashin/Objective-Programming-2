#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from my_module.k21099.lecture06_camera_image_capture import MyVideoCapture

def lecture06_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('google.png')
    # capture_img : cv2.Mat = cv2.imread('camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img : cv2.Mat = app.get_img()

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                x_hight = x%c_width
                y_width = y%c_hight
                google_img[y,x] = capture_img[y_width,x_hight]
    cv2.imwrite('lecture06_01_k21099.png',google_img)

if __name__ == "__main__":
    lecture06_01()
