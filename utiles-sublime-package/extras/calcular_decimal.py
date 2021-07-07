#!/usr/bin/python3
# -*- coding:utf8 -*- 

# referencia : https://code.tutsplus.com/es/tutorials/mathematical-modules-in-python-decimal-and-fractions--cms-27691

from decimal import Decimal
from sys import argv


def calcularDecimal(t):
	s = ' '
	ps = t.strip().split(s)
	os = ['+', '-', '*', '**', '/', '//', '(', ')']
	r = []
	for p in ps:
		if not p == '':
			if not p in os:
				p = "Decimal('{}')".format(p)
			r.append(p)
	return eval(s.join(r))



if __name__ == '__main__':
    if len(argv) > 1:
        for a in argv[1:]:
            try:
                print(calcularDecimal(a))
            except Exception as e:
                print(e)