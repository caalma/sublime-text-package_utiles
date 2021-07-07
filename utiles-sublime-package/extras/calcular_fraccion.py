#!/usr/bin/python3
# -*- coding:utf8 -*- 

from fractions import Fraction
from sys import argv


def calcularFraccion(t):
    s = ' '
    ps = t.strip().split(s)
    os = ['+', '-', '*', '**', '/', '//', '(', ')']
    r = []
    for p in ps:
        if not p in os:
            p = "Fraction('{}')".format(p)
        r.append(p)
    return eval(s.join(r))


if __name__ == '__main__':
    if len(argv) > 1:
        for a in argv[1:]:
            try:
                print(calcularFraccion(a))
            except Exception as e:
                print(e)