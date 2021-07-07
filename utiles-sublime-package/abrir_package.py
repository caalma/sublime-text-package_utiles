# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import realpath, dirname
import webbrowser 


class abrirpkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        rpk = dirname(realpath(__file__))
        webbrowser.open(rpk)