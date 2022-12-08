#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('uchitane_near.png',cv2.IMREAD_COLOR)
rows, cols, channels = img.shape
# print(f"画像の大きさは幅{cols}px x 縦{rows}px")
mask = np.zeros((rows, cols, channels), dtype=np.uint8)
mask[0:int(rows/2),:] = [255 for i in range(channels)] # yの上半分を白に，下半分は黒(0,0,0)のまま

# このプログラムの主役
# imgの特定の領域だけを切り出すようにmask画像を利用する
img_AND = cv2.bitwise_and(img, mask)

cv2.imshow('masked_img',img_AND)
cv2.waitKey(0) # なにかキーが押されるまで待機
cv2.destroyAllWindows()