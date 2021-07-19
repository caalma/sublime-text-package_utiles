import sublime
import sublime_plugin
from os.path import dirname
from subprocess import Popen


if 'linux' == sublime.platform():
    cmd = ['terminator', '--working-directory']

if 'windows' == sublime.platform():
    cmd = ['cmd']


class AbrirTerminalCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        r = [dirname(self.view.window().active_view().file_name())]
        Popen(cmd + r)