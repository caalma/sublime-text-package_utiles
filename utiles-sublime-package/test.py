# -*- coding:utf8 -*- 

import sublime
import sublime_plugin


class testCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            tex = self.view.substr(region).strip()
            extra = 'TEST'
            tex = ' # {} {}'.format(extra, data)
            self.view.insert(edit, posfin, tex)
