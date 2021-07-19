import sublime
import sublime_plugin
from os.path import dirname, join
from subprocess import Popen, PIPE


if 'linux' == sublime.platform():
    cmd_python = 'python3'
    
if 'windows' == sublime.platform():
    cmd_python = 'python'


class YoutubeTitleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            url = self.view.substr(region).strip()
            script = join(dirname(__file__),'extras/yt_info.py')
            proc = Popen([cmd_python, script, url, 'title'], shell=False, stdout=PIPE)
            title = proc.stdout.read().decode('utf-8').strip().replace('\n', ' - ')
            text = ' # {}'.format(self.__clean(title))
            self.view.insert(edit, region.end(), text)

    def __clean(self, text):
        ree = [
            ['|', '-'],
        ]
        
        for r in ree:
            text = text.replace(r[0],r[1])

        return text