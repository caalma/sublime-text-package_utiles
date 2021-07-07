# -*- coding:utf8 -*- 

import sublime
import sublime_plugin


class sumartiemposCommand(sublime_plugin.TextCommand):

    def sumar_tiempos(self, t):
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

    def run(self, edit):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            tex = self.view.substr(region).strip()
            extra = self.sumar_tiempos(tex)
            tex = ' = {}'.format(extra)
            self.view.insert(edit, posfin, tex)