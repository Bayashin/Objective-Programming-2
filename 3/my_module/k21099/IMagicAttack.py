import abc
from my_module.k21099.lecture03_hero import Hero

class IMagicAttack(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def damage(self, enemy : Hero) -> None:
        """
        魔法攻撃のダメージを敵に与える
        ダメージを与えた後にHPが0以下になったenemyを削除する

        Parameters
        ----------
        enemy : Hero
            ダメージを与えるHero
        """
        raise NotImplementedError()