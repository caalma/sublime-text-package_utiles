# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE
import math
from math import *
import platform


if 'Linux' == platform.system():
    python = 'python3'

if 'Windows' == platform.system():
    python = 'python'


class calcularCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            rtex = self.view.substr(region).strip()

            res = []
            if rtex == 'math':
                res.append(', '.join(dir(math)))
            else:
                sep = ';' if ';' in rtex else '\n'
                ll = rtex.split(sep)
                for l in ll:
                    if '=' in l:
                        exec(l)
                        v = l.split('=')[0].strip()
                        res.append('{} = {}'.format(v, eval(v)))
                    elif l.strip() == '':
                        res.append('')
                    else:
                        res.append('{} = {}'.format(l, eval(l)))

            tex = '\n\n{}'.format('\n'.join(res))

            self.view.insert(edit, posfin, tex)


class calcularfraccionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            rtex = self.view.substr(region)
            script = join(dirname(__file__), 'extras/calcular_fraccion.py')

            p = Popen([python, script, rtex], shell=False, stdout=PIPE, stderr=PIPE)
            res = p.stdout.read().decode('utf-8').strip().replace('\n', ' - ')       
            tex = ' = {}'.format(res)

            self.view.insert(edit, posfin, tex)


class calculardecimalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            rtex = self.view.substr(region)
            script = join(dirname(__file__), 'extras/calcular_decimal.py')

            p = Popen([python, script, rtex], shell=False, stdout=PIPE, stderr=PIPE)
            res = p.stdout.read().decode('utf-8').strip().replace('\n', ' - ')            
            tex = ' = {}'.format(res)

            self.view.insert(edit, posfin, tex)