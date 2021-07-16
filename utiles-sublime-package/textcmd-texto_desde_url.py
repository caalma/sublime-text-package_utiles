# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE
import platform


if 'Linux' == platform.system():
    python = 'python3'

if 'Windows' == platform.system():
    python = 'python'


class textodesdeurlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        url = self.view.substr(region).strip()
        posfin = region.end()
        script = join(dirname(__file__), 'extras/extraer_texto_de_url.py')

        p = Popen([python, script, url], shell=False, stdout=PIPE, stderr=PIPE)
        tex = '\n'+p.stdout.read().decode('utf-8')
        self.view.insert(edit, posfin, tex)