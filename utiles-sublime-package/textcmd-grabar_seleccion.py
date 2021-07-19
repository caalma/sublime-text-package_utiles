import sublime
import sublime_plugin
import webbrowser
from os.path import dirname, splitext


class GrabarSeleccionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file = self.view.window().active_view().file_name()
        sublime.save_dialog(self.__save, 
            directory = dirname(file), 
            name = 'filename', 
            extension = splitext(file)[1].strip('.')
            )

    def __save(self, filename):
        if filename:
            region = self.view.sel()[0]
            with open(filename, 'w') as f:
                f.write(self.view.substr(sublime.Region(region.a, region.b)))
                sublime.status_message('Grabado en : {}'.format(filename))