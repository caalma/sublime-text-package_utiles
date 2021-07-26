import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE


if 'linux' == sublime.platform():
    python = 'python3'

if 'windows' == sublime.platform():
    python = 'python'


class TextFromUrlCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        url = self.view.substr(region).strip()
        script = join(dirname(__file__), 'extras/extraer_texto_de_url.py')
        process = Popen([python, script, url], shell=False, stdout=PIPE)
        text = '\n{}'.format(process.stdout.read().decode('utf-8'))
        self.view.insert(edit, region.end(), text)