from my_module.k21099.lecture03_hero import Hero
from my_module.k21099.IMagicAttack import IMagicAttack

# HeroクラスとIMagicAttackクラスを継承したMagician2クラスを宣言
class Magician2(Hero, IMagicAttack): 

    __DEFAULT_MP = 100

    # コンストラクタ
    def __init__(self, name=None, hp=Hero.getDefaultHP(), mp=__DEFAULT_MP):
        super().__init__(name, hp)
        self.mp = mp

    # 特殊な関数の宣言(上書き)
    def __str__(self):
        return f'"名前": "{self.name}", "HP": {self.getHP()}, "MP": {self.mp}'

    # 抽象クラスのメソッドを実装する
    # def damage(self, enemy: Hero) -> None:
    #     print(f"{self.name}は{enemy.name}に100のダメージ")
    #     enemy.hp -= 100
    #     # bufを含めhpが0以下の場合は離脱させる
    #     if(enemy.getHP() <= 0):
    #         del(enemy)

if __name__ == '__main__':
    hero3 = Magician2(name='愛知さぶろう', hp=10)
    hero3.damage(hero3) # 実装したのでエラーではなくhpが減り離脱する