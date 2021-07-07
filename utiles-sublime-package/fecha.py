# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from datetime import datetime


class fechaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        r = self.view.sel()[0]
        pos = min(r.a, r.b)
        tex = str(datetime.now())
        self.view.insert(edit, pos, tex)


class duracionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            s = ';'
            rtex = self.view.substr(region).strip(s).split(s)
            i1, i2 = [datetime.fromtimestamp(float(v)) for v in rtex]
            du = abs(i2 - i1)
            se = int(du.total_seconds())
            sim = 60
            sih = sim * sim
            ho = int(se / sih)
            se = se - (ho * sih)
            mi = int(se / sim)
            se = se - (mi * sim)
            tex = '{:02}h {:02}m {:02}s'.format(ho, mi, se)
            self.view.insert(edit, posfin, tex)


class instanteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            pos = min(s.a, s.b)
            ins = datetime.now().timestamp()
            tex = '{};'.format(ins)
            self.view.insert(edit, pos, tex)


class instanteafechaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            tex = self.view.substr(region).strip()
            timestamp = float(tex.strip().strip(';'))
            tiempo = datetime.fromtimestamp(timestamp)
            extra = str(tiempo.strftime("%Y-%m-%d"))
            tex = ' {}'.format(extra)
            self.view.insert(edit, posfin, tex)


class instanteahoraCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            tex = self.view.substr(region).strip()
            timestamp = float(tex.strip().strip(';'))
            tiempo = datetime.fromtimestamp(timestamp)
            extra = str(tiempo.strftime("%H:%M:%S"))
            tex = ' {}'.format(extra)
            self.view.insert(edit, posfin, tex)