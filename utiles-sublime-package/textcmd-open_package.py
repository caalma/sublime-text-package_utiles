import sublime
import sublime_plugin
from os.path import realpath, dirname
import webbrowser 


class OpenPackageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        webbrowser.open(dirname(realpath(__file__)))