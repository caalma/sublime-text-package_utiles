# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from datetime import datetime


class FechaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        init = min(region.a, region.b)
        text = str(datetime.now())
        self.view.insert(edit, init, text)


class DuracionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
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
            text = '{:02}h {:02}m {:02}s'.format(ho, mi, se)
            self.view.insert(edit, region.end(), text)


class InstanteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            init = min(region.a, region.b)
            now = datetime.now().timestamp()
            text = '{};'.format(now)
            self.view.insert(edit, init, text)


class InstanteComoFechaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            text_input = self.view.substr(region).strip()
            timestamp = float(text_input.strip().strip(';'))
            date = datetime.fromtimestamp(timestamp)
            text = ' {}'.format(date.strftime("%Y-%m-%d"))
            self.view.insert(edit, region.end(), text)


class InstanteComoHoraCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            text_input = self.view.substr(region).strip()
            timestamp = float(text_input.strip().strip(';'))
            date = datetime.fromtimestamp(timestamp)
            text = ' {}'.format(date.strftime("%H:%M:%S"))
            self.view.insert(edit, region.end(), text)


class SumarTiemposCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            text_input = self.view.substr(region).strip()
            text = ' = {}'.format(self.__add(text_input))
            self.view.insert(edit, region.end(), text)

    def __add(self, t):
        lin = t.strip().split('\n')
        dat = [l.strip().split(' ') for l in lin]
        elem = { 'h': [], 'm': [], 's': []}
        for tie in dat:
            for el in tie:
                try:
                    elem[el[-1]].append(int(el[0:-1]))
                except Exception as e:
                    return '!ERROR de formato!'
        t_se = sum(elem['s'])
        segu = t_se % 60
        t_mi = sum(elem['m']) + (t_se // 60)
        minu = t_mi % 60 
        hora = sum(elem['h']) + (t_mi // 60)
        res = '{:02}h {:02}m {:02}s'.format(hora, minu, segu)
        return res
