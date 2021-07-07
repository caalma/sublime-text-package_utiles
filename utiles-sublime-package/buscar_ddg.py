# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from subprocess import Popen, PIPE
import platform


if 'Linux' == platform.system():
    wb = False
    cmd = 'xdg-open'

if 'Windows' == platform.system():
    wb = True
    import webbrowser


class buscarDdgCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            bus = self.view.substr(region).strip()
            url = 'http://duckduckgo.com?q={}'.format(bus.replace(' ', '+'))
            if wb:
                webbrowser.open_new_tab(url)
            else:
                Popen([cmd, url], shell=False)
