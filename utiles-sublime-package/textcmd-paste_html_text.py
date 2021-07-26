import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE


if 'linux' == sublime.platform():
    available = True
    python = 'python3'

if 'windows' == sublime.platform():
    available = False


if available:
    class PasteHtmlTextCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            region = self.view.sel()[0]
            url = self.view.substr(region).strip()
            script = join(dirname(__file__), 'extras/clipboard_text_html.py')
            process = Popen([python, script], shell=False, stdout=PIPE)
            text = '{}'.format(process.stdout.read().decode('utf-8'))
            self.view.insert(edit, region.end(), text)