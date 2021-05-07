# !/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    pr = input("Введите предложение: ")
    s = 0
    for i in pr:
        if i.isdigit():
            s += int(i)
    print(s)