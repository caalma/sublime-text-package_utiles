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


class yttituloCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            url = self.view.substr(region).strip()
            script = join(dirname(__file__),'extras/yt_info.py')

            p = Popen([python, script, url, 'title'], shell=False, stdout=PIPE, stderr=PIPE)
            tit = p.stdout.read().decode('utf-8').strip().replace('\n', ' - ')

            tex = ' # {}'.format(tit)
            self.view.insert(edit, posfin, tex)