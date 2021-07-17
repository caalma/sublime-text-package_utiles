import sublime
import sublime_plugin
import webbrowser
from os.path import exists, realpath, dirname, join, expanduser

class grabarseleccionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.select_folder_dialog(self.save)

    def save(self, folder):
        ss = self.view.sel()
        for i, s in enumerate(ss):
            name = '{:03d}'.format(i)
            with open(join(folder, name), 'w') as f:
                f.write(self.view.substr(sublime.Region(s.a, s.b)))