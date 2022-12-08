const init = () => {
    // データの初期表示
    fetch("/address").then(response => {
        console.log(response)
        response.json().then((data) => {
            console.log(data) // 取得されたレスポンスデータをデバッグ表示
            show_data(data)
        })
    })

    // エラーの表示領域を初期化
    document.getElementById('error-container').innerHTML = ""
    document.getElementById('error-container').style.display = "none"
    // 登録メッセージ等の表示領域を初期化
    document.getElementById('message-container').innerHTML = ""
    document.getElementById('message-container').style.display = "none"

}

// データ表示を関数化
const show_data = (data) => {
    // データを表示させる
    const tableBody = document.querySelector("#address-list > tbody")
    tableBody.innerHTML = ""

    // レスポンスのJSONデータの件数が0だった場合
    if (data && data.length == 0) {
        let tr = document.createElement('tr')
        tr.innerHTML = "表示するデータがありません。"
        tableBody.appendChild(tr)
        return
    }

    data.forEach(elm => {
        let tr = document.createElement('tr')
        // first name
        let td = document.createElement('td')
        td.textContent = elm.first_name
        tr.appendChild(td)
        // last name
        td = document.createElement('td')
        td.textContent = elm.last_name
        tr.appendChild(td)
        // email
        td = document.createElement('td')
        td.textContent = elm.email
        tr.appendChild(td)

        // 1行分をtableタグ内のtbodyへ追加する
        tableBody.appendChild(tr)
    })
}


// 初期化処理の呼び出し
init()

// 検索ボタンクリック時の動作設定
document.getElementById("search-submit").addEventListener("click", (e) => {
    // 現在動作中のクリックイベント以外のボタンイベントをキャンセル
    e.preventDefault()

    // GETパラメータの構築をURLSearchParams APIで行う
    let params = new URLSearchParams()
    let fn = document.getElementById("search-firstname").value
    let ln = document.getElementById("search-lastname").value
    let em = document.getElementById("search-email").value
    if (fn && fn !== "") params.set("fn", fn)
    if (ln && ln !== "") params.set("ln", ln)
    if (em && em !== "") params.set("em", em)

    fetch("/address?" + params.toString()).then(response => {
        console.log(response)
        response.json().then((data) => {
            console.log(data) // 取得されたレスポンスデータをデバッグ表示
            show_data(data)
        })
    })
})


// Addボタンクリック時の動作設定
document.getElementById("add-submit").addEventListener("click", (e) => {
    // ボタンイベントのキャンセル
    e.preventDefault()

    // 入力チェック
    let fn = document.getElementById("add-firstname").value
    let ln = document.getElementById("add-lastname").value
    let em = document.getElementById("add-email").value

    // 未入力がある項目ごとにエラーメッセージを積み上げる
    let error_message = ""
    if (!fn && fn === "") error_message += "first nameが未入力です。<br>"
    if (!ln && ln === "") error_message += "last nameが未入力です。<br>"
    if (!em && em === "") error_message += "emailが未入力です。<br>"

    // エラーメッセージがあるかどうかでエラーの表示有無を決定
    if (error_message !== "") {
        document.getElementById('error-container').innerHTML = error_message
        document.getElementById('error-container').style.display = "block"
        return
    } else {
        document.getElementById('error-container').innerHTML = ""
        document.getElementById('error-container').style.display = "none"
    }

    // データ送信
    // FormDataのコンストラクタを使い、フォームデータを一括取得(form内の各inputタグにname属性を正しく設定する必要があります)
    let data = new FormData(document.getElementById('add'))
    /* こちらのやり方でもOK
    let data = new FormData()
    data.append("fn", fn)
    data.append("ln", ln)
    data.append("em", em)
    */
    fetch('/address', {
        method: 'POST',
        body: data,
    }).then((response) => {

        // 入力項目の初期化
        document.getElementById("add").reset()
        
        // エラーの表示領域を初期化
        document.getElementById('error-container').innerHTML = ""
        document.getElementById('error-container').style.display = "none"
        // 登録メッセージ等の表示領域を初期化
        document.getElementById('message-container').innerHTML = ""
        document.getElementById('message-container').style.display = "none"

        // レスポンスデータからJSONを取り出し
        response.json().then((data) => {

            if (data.error) {
                // エラーの受信
                document.getElementById('error-container').innerHTML = data.error
                document.getElementById('error-container').style.display = "block"
            }

            if (data.result) {
                // メッセージの受信
                document.getElementById('message-container').innerHTML = data.result
                document.getElementById('message-container').style.display = "block"
                if (data.json_data) {
                    show_data(data.json_data)
                }
            }
        })
    })
})