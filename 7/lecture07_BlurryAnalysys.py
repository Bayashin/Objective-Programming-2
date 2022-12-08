import cv2

BLURRY_THRESHOLD = 90 # 値が低いほど少しのボケでも検出する

# カメラに近い画像（uchitane_far.png）と遠い画像（uchitane_far.png）を開く
# このプログラムは同じサイズの画像を読み込んで下さい．
near_img = cv2.imread('uchitane_near.png')
far_img = cv2.imread('uchitane_far.png')

near_rows,near_cols,near_channels = near_img.shape
far_rows,far_cols,far_channels = far_img.shape

near_gray = cv2.cvtColor(near_img, cv2.COLOR_BGR2GRAY)
far_gray = cv2.cvtColor(far_img, cv2.COLOR_BGR2GRAY)

if near_rows != far_rows or near_cols != far_cols:
    print("入力ファイルのサイズが違います")
    quit()

# 画像の大きさが等しいので，変数名を変更
hight=near_rows
width=near_cols

# それぞれの画像に対して何かしらの分析を実施
# 3x3の畳み込みフィルターをかけて画像のボケを判定する
near_laplacian = cv2.Laplacian(near_gray, cv2.CV_64F) #ラプラシアン値
far_laplacian = cv2.Laplacian(far_gray, cv2.CV_64F) #ラプラシアン値

print(f"uchitane_nearのlaplacian.var()の値は={near_laplacian.var()}")
print(f"uchitane_farのlaplacian.var()の値は={far_laplacian.var()}")
# print(type(near_laplacian))
# print(near_laplacian.shape)
# print(near_laplacian[0:10,0:10])
# print(near_laplacian.max())
# print(near_laplacian.min())

# 出力用に画像をコピー
output_img = near_img.copy()
# 出力画像の右半分を他方の画像で置き換え
output_img[0:hight, (int)(width/2):] = far_img[0:hight, (int)(width/2):]

if near_laplacian.var() < BLURRY_THRESHOLD: # ここでは閾値以下だとピンボケ画像と判定
    near_text = "Blurry"
else: 
    near_text = "Not Blurry"

if far_laplacian.var() < BLURRY_THRESHOLD: # ここでは閾値以下だとピンボケ画像と判定
    far_text = "Blurry"
else:
    far_text = "Not Blurry"

# 左の画像に分析結果を表示
cv2.putText(output_img, f"{near_text}: {near_laplacian.var():.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)
# 右の画像に分析結果を表示
cv2.putText(output_img, f"{far_text}: {far_laplacian.var():.2f}", (width - 10 - 250, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 3)

# 分析結果を出力
cv2.imwrite("blurry_analysis_result.png", output_img)
# 編集した画像を表示する
cv2.imshow('analysis_result', output_img)

# 終了処理
cv2.waitKey(0)
cv2.destroyAllWindows()
