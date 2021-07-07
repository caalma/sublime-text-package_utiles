# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import dirname, realpath, exists, expanduser, join
from subprocess import Popen, PIPE
import webbrowser


class abrirArchivoCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        ss = self.view.sel()
        for s in ss:
            region = s
            posfin = s.end()
            urr = self.view.substr(region).strip()
            if not urr.startswith('/'):
                art = self.view.window().active_view().file_name()
                ruta = dirname(art) if art else expanduser('~')
                urr = join(ruta, urr)

            uri = realpath(urr)
            if exists(uri):
                webbrowser.open(uri)