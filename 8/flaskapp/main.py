from flask import Flask, request #Flaskは必須、requestはリクエストパラメータを処理する場合に使用する
app = Flask(__name__)

#http://localhost:8080/hello
#http://127.0.0.1:8080/hello
@app.route('/hello')
def hello():
    return "<html><h1>Hello, Flask!!</h1></html>"

#GETパラメータの取得（クエストリングより）
#http://localhost:8080/
@app.route('/')
def index():
    html = "<html><h3>index page</h3></ol>"

    #URL中のクエストリングを処理（個別に種録したい場合は、request.args.get("hoge")が使えます）
    for key,  value in request.args.items():
        html += "<li>{} : {}</li>".format(key, value)

    html += "</ol></html>"
    return html

#GETパラメータの取得
#http://localhost:8080/get/
#http://localhost:8080/get/<name>
@app.route('/get')
@app.route('/get/<name>')
def get_param(name='no name'): #nameパラメータが渡されなかった場合、「no name」が渡される
    return "<html><h1>Hello, {}!!</h1></html>".format(name)

#GET,POSTどちらでもリクエストを受付,POSTの場合はリクエストボディを取得
#（コマンドラインでの動作確認は、$ curl -X POSR -d "name=hoge" http://localhost:8080/post/ でできる
# http://localhost:8080/post/
@app.route('/post', methods=["GET", "POST"]) # methods = ["POST"] のみにすればGETメソッドでのリクエストはエラーにできる
def post_param():
    if request.method == 'POST':
        # name = request.form['name']
        name = request.form.get("name")
        return "<html><h1>Hello, {}!!</h1></html>".format(name)
    else:
        name = "no name"
        return "<html><h1>Hello, {}!!</h1></html>".format(name)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8080, debug=True)