import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE
import math
from math import *


if 'linux' == sublime.platform():
    python = 'python3'

if 'windows' == sublime.platform():
    python = 'python'


class CalcularCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            text_input = self.view.substr(region).strip()
            res = []
            if text_input == 'math':
                res.append(', '.join(dir(math)))
            else:
                sep = ';' if ';' in text_input else '\n'
                ll = text_input.split(sep)
                for l in ll:
                    if '=' in l:
                        exec(l)
                        v = l.split('=')[0].strip()
                        res.append('{} = {}'.format(v, eval(v)))
                    elif l.strip() == '':
                        res.append('')
                    else:
                        res.append('{} = {}'.format(l, eval(l)))

            text = '\n\n{}'.format('\n'.join(res))
            self.view.insert(edit, region.end(), text)


class CalcularFraccionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            text_input = self.view.substr(region)
            script = join(dirname(__file__), 'extras/calcular_fraccion.py')
            process = Popen([python, script, text_input], shell=False, stdout=PIPE)
            resp = process.stdout.read().decode('utf-8').strip().replace('\n', ' - ')       
            text = ' = {}'.format(resp)
            self.view.insert(edit, region.end(), text)


class CalcularDecimalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            text_input = self.view.substr(region)
            script = join(dirname(__file__), 'extras/calcular_decimal.py')
            process = Popen([python, script, text_input], shell=False, stdout=PIPE)
            resp = process.stdout.read().decode('utf-8').strip().replace('\n', ' - ')            
            text = ' = {}'.format(resp)
            self.view.insert(edit, posfin, text)