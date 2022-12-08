#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_module.k21099.lecture03_hero import Hero
from my_module.k21099.lecture03_magician2 import Magician2

if __name__ == '__main__':
    hero = Hero(name="愛知太郎", hp=1000)
    print(hero)
    magician = Magician2(name="愛知次郎", hp=200, mp=100)
    print(magician)