# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE
import platform


if 'Linux' == platform.system():
    disponible = True
    python = 'python3'

if 'Windows' == platform.system():
    disponible = False


if disponible:
    class pegarhtmltextCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            region = self.view.sel()[0]
            url = self.view.substr(region).strip()
            posfin = region.end()
            script = join(dirname(__file__), 'extras/clipboard_text_html.py')

            p = Popen([python, script], shell=False, stdout=PIPE, stderr=PIPE)
            res = p.stdout.read().decode('utf-8')
            tex = '{}'.format(res)

            self.view.insert(edit, posfin, tex)