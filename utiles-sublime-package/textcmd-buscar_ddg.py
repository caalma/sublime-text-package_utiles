# -*- coding:utf8 -*- 

import sublime
import sublime_plugin


class buscarddgCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            bus = self.view.substr(region).strip()
            url = 'http://duckduckgo.com?q={}'.format(bus.replace(' ', '+'))
            webbrowser.open_new_tab(url)