import sublime
import sublime_plugin
import webbrowser
from os.path import dirname, splitext, expanduser


class SaveSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, text_input):
        self.save_mode = 'a' if text_input == 'A' else 'w'
        self.init_text = '\n\n' if self.save_mode == 'a' else ''

        file = self.view.window().active_view().file_name()
        
        file = expanduser('~') if file == None else dirname(file)
        sublime.save_dialog(self.__save, 
            directory = file, 
            name = 'filename', 
            extension = splitext(file)[1].strip('.')
            )

    def __save(self, filename):
        if filename:
            region = self.view.sel()[0]
            with open(filename, self.save_mode) as f:
                f.write(self.init_text + self.view.substr(sublime.Region(region.a, region.b)))
                sublime.status_message('Grabado en : {}'.format(filename))

    def input(self, args):
        return TestTextInputHandler(self.view)
 

class TestTextInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view

    def initial_text(self):
        return 'A'

    def name(self):
        return 'text_input'

    def placeholder(self):
        return 'Texto a insertar'

    def preview(self, text):
        return '¿ [ A ]gregar o [ R ]eemplazar ?'