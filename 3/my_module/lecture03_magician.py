from my_module.k21099.lecture03_hero import Hero

# Heroクラスを継承したMagicianクラスを宣言
class Magician(Hero): 

    __DEFAULT_MP = 100

    # コンストラクタ
    # 親クラスのコンストラクタをsuper().__init__()で呼び出すことができる
    # 親クラスのprivate変数にアクセスする方法１としてDEFAULT_HPのゲッター関数を呼び出している
    def __init__(self, name=None, hp=Hero.getDefaultHP(), mp=__DEFAULT_MP):
        super().__init__(name, hp)
        self.mp = mp

    # 特殊な関数の宣言(上書き)
    def __str__(self):
        return f'"名前": "{self.name}", "HP": {self.hp + self.buf_status["hp"]}, "MP": {self.mp}'

    # 親クラスのprivate変数へのアクセス
    def printDefaultHP(self):
        # 親クラスのprivate変数にアクセスする方法2
        print(f"親クラスのプライベート変数にアクセス: DEFAULT_HP={Hero._Hero__DEFAULT_HP}")

if __name__ == '__main__':
    hero1 = Hero('愛知太郎') # Heroクラスのインスタンスを生成
    print(f'hero1={str(hero1)}') # 文字列に変換
    hero2 = Magician(name='愛知花子', hp=200, mp=200) # 引数名を指定してコンストラクタを呼び出し
    print(f'hero2={str(hero2)}') # 文字列に変換
    hero2.printDefaultHP()
    print(type(hero1)) # <class 'my_module.lecture03_hero.Hero'>
    print(type(hero2)) # <class '__main__.Magician'>
    if type(hero1) is Hero:
        print('hero1はHero')
    if type(hero2) is not Hero:
        print('hero2とはHeroではない')
    if isinstance(hero1, Hero):
        print('hero1はHeroクラスのインスタンス')
    if isinstance(hero2, Hero):
        print('hero2もHeroクラスのインスタンス')