# !/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    pr = input("Предложение: ").lower().split()
    for word in pr:
        if pr.count(word) == 2:
            sl = word
    print(f"{sl}")
