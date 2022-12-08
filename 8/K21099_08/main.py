from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
import datetime #日時取得のライブラリ

app = Flask(__name__)

# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route('/')
def index():
    return render_template('index.html')


# 2. アプリの入力フォーム
@app.route('/janken')
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template('janken_form.html')

@app.route('/uranai')
def uranai():
    # 占いデータの入力画面のテンプレートを呼び出し
    return render_template('uranai_form.html')


# 3. データ送信先と結果表示画面
@app.route('/janken/play', methods=["POST"])
def janken_play():

    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    if not name:
        name = "名無しさん"
    
    # <input type="radio" id="hand_rock" value="rock" name="hand">
    # <input type="radio" id="hand_scissor" value="scissor" name="hand">
    # <input type="radio" id="hand_paper" value="paper" name="hand">
    hand = request.form.get("hand", None)
    check = request.form.get("settai")

    # リストの中からランダムに選ぶ
    cpu = random.choice(["rock", "scissor", "paper"])

    if check == "on":
        if hand == "rock" or hand == None:
            hand = "rock"
            cpu = "scissor"
        elif hand == "scissor":
            cpu = "paper"
        else:
            cpu = "rock"


    # じゃんけん処理
    result = False
    if hand == cpu:
        result_message = "あいこ"
    else:
        if hand == "rock":
            if cpu == "scissor":
                result = True
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "scissor":
            if cpu == "paper":
                result = True
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "paper":
            if cpu == "rock":
                result = True
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        else:
            result_message = "後出しはダメです。"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template('janken_play.html',
                            result_message=result_message,
                            name=name,
                            hand=hand,
                            cpu=cpu,
                            result=result)

@app.route('/uranai/play', methods=["POST"])
def uranai_play():
    #名前の取得
    name = request.form.get("name")
    #生年月日の取得
    birth = request.form.get("birthday")
    # 現在日時を取得するオブジェクトの取得
    dt_now = datetime.datetime.now()

    #名前または生年月日の入力不備で占い不可
    if not name or not birth:
        result = 1
        result_message = "入力不備で占えませんでした"

    #生年月日を数値化する
    birth_num = birth.replace('-','')
    #現在の日付を数値として取得する
    today_num = str(dt_now.year) + str(dt_now.month) + str(dt_now.day)
    #数値化した現在日付から生年月日を減算し、結果の絶対値を算出する
    date = abs(int(today_num) - int(birth_num))
    #「減算結果の絶対値」と「名前の文字数」を掛け算にて算出する
    data2 = date * len(name)
    #「掛け算結果を5で割った余り」をList:[5, 1, 3, 2, 4]のインデックスとして使用し取り出した数値要素を占い結果とする
    list = [5, 1, 3, 2, 4]
    index = data2 % 5
    result = list[index]

    #1〜5の数値で得られる5段階の占い結果に対して、それぞれ各段階における適当なメッセージも添えること
    if result == 1:
        result_message = "残念、今日は何してもうまくいかないよ"
    elif result == 2:
        result_message = "よくないことが起きるかも？"
    elif result == 3:
        result_message = "いつも通りの生活を送ろう"
    elif result == 4:
        result_message = "何かいいことが起きるかも"
    elif result == 5:
        result_message = "今日以上に幸運な日はない！"

    return render_template('uranai_play.html',
                            result=result,
                            result_message=result_message)


if __name__ == '__main__':
    app.run()