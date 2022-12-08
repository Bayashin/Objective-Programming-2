#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import A


def lecture01_01() -> None:
    h={}
    h["ID"] = 'k21099'
    h["attributes"] = ("林航平", 20, "男")
    print(h)
    print(h.keys())
    print(type(h.keys()))
    print(type(h["attributes"]))
    for e in h["attributes"]:
        print(e)
    for e in h["attributes"]:
        print(type(e))

if __name__ == '__main__':
    lecture01_01()

