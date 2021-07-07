# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import dirname
from subprocess import Popen
import platform


if 'Linux' == platform.system():
    cmd = ['terminator', '--working-directory']

if 'Windows' == platform.system():
    cmd = ['cmd']


class abrirTerminalCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        r = [dirname(self.view.window().active_view().file_name())]
        Popen(cmd + r)