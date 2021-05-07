#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':

    pr = input("Введите предложение: ")
    o = pr.lower().count('о')
    a = pr.lower().count('а')

    if (o > a):
        print(f"'o' в предложении больше ({o})")
    elif (o < a):
        print(f"'a' в предложении больше ({a})")
    elif (o == a):
        print(f"'a' ({a}) = 'o' ({o})")
    else:
        print("ошибка", file=sys.stderr)
        exit(1)