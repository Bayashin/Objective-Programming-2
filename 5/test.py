#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def read_csv04():
    data = []
    with open('sample.csv') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i> 0:
                data.append([(int)(e) for e in row])
    print(data)

read_csv04()