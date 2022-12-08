#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ↑はシバンと文字コードの指定（説明はしないけど大切なので調べてみて欲しい）

# クラスを「class 〇〇」で宣言する
class Hero:
    """
    HeroクラスはOOP2の学習のために作ったサンプルコードです

    Attributes
    ----------
    name : str
        Heroの名前　インスタンス作成時に指定する
    hp : int, default is __DEFAULT_HP = 100
        Heroの初期HP　指定しない場合はデフォルト値となる
    """

    # Javaでいうstatic変数
    # クラスのインスタンスを作らなくてもアクセスできる
    # 定数は大文字アルファベットなどルールを設けることが多い
    # 複数のHeroインスタンスのjob_statusは共通なのでHero職へのバフに使う
    # 例：Hero全体のステータスの向上はjob_status値を変更
    __DEFAULT_HP = 100
    buf_status = {'hp': 0}

    # コンストラクタ
    # デフォルト値を指定することもできる
    # なお，引数が異なるコンストラクタを定義することはできない
    def __init__(self, name, hp=__DEFAULT_HP):
        """
        コンストラクタ

        Parameters
        ----------
        name : str
            デフォルト値が設定されていないので必ず必要
        hp : int
            デフォルト値は全ヒーロー共通で__DEFAULT_HPとする
        """
        self.name = name # クラス内の変数を「self.変数名」で宣言する（コンストラクタ以外でも宣言可能）
        self.hp = hp
        self.__weapon_id = None # アンダーバーを2個つけるとprivate（武器は未実装）


    # デストラクタ
    def __del__(self):
        # 3項演算子（1行でif文を書く： 真のときの返り値 if 条件 else 偽のときの返り値）
        message = '一時パーティー離脱' if self.getHP()>0 else '死亡のためパーティー離脱'
        print(f'{self.name}は{message}')


    # 特殊な関数の宣言
    def __str__(self):
        return f'"名前": "{self.name}", "HP": {self.getHP()}'


    # bufの影響を計算してhpを返すメソッド
    def getHP(self) -> int:
        """
        ヒーロのHPをbutを考慮して返す

        Returens
        --------
        hp : int
            HPに関係したbufが存在すればbufを加えてHPを返す
        """
        if 'hp' in Hero.buf_status.keys():
            return self.hp + Hero.buf_status['hp']
        else:
            return self.hp


    # DefaultHPのゲッター(selfを引数に入れないとstatic扱い)
    def getDefaultHP() -> int:
        """
        privateかつstaticな変数__DEFAULT_HPのゲッター
        """
        return Hero.__DEFAULT_HP


    # 別のHeroクラスのインスタンスを受け取り，ダメージを与えるメソッド
    # 未開発です
    def damage(self, enemy):
        raise NotImplementedError()


if __name__ == '__main__':
    hero1 = Hero('愛知太郎') # Heroクラスのインスタンスを生成，後に()がついているのは関数呼び出しかクラスインスタンス生成
    print(f'hero1={str(hero1)}') # 文字列に変換
    hero2 = Hero(name='愛知花子', hp=200) # 引数名を指定してコンストラクタを呼び出し
    print(f'hero2={str(hero2)}') # 文字列に変換

    # クラスメソッドの内，第1引数にselfが書かれているメソッドはインスタンスを作成して初めて呼び出せる
    print(f'hero1のHPは{hero1.getHP()}')

    # __DEFAULT_HPはPrivate変数なので直接アクセスするとエラーになる(↓の行のコメントを実行してみましょう)
    # print(Hero.__DEFAULT_HP) # private変数にアクセスできてしまうのであくまでもprivate扱いして欲しい変数
    # classの外からprivate変数にアクセスしたければアクセサー（get, set)を作ります
    print(Hero.getDefaultHP()) # static扱いの変数はインスタンス化しなくても実行可能

    print("Hero全員のHPが下がるトラップ（デバフ）発動") # フレーバーテキスト
    # buf_statusはJavaでいうstaticな変数なのでインスタンス化しなくてもアクセスできる
    Hero.buf_status['hp'] -= 50 # hero1にもhero2にも今後作られるHeroインスタンスにもデバフがかかる
    print(f'hero1のHPは{hero1.getHP()}')
    print(f'hero2のHPは{hero2.getHP()}')
    print("hero1はHero全員のHPが下がる呪い（デバフ）をうけた") # フレーバーテキスト
    hero1.buf_status['hp'] -= 50 # hero1にもhero2にも今後作られるHeroインスタンスにもデバフがかかる
    print(f'Hero.job_status = {Hero.buf_status}') # Heroクラスのjob_statusの値が変わる
    print(f'hero1={str(hero1)}') # 文字列に変換
    del hero1 # インスタンスを削除=>死亡のためパーティー離脱
    print(f'hero2={str(hero2)}') # 文字列に変換
    del hero2 # インスタンスを削除=>一時パーティー離脱
    hero3 = Hero(name='愛知さぶろう', hp=10)
    hero3.damage(hero3) # 実装していないので例外(raise)が呼び出される
