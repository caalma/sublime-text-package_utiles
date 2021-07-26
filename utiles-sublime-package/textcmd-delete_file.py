import sublime
import sublime_plugin
from os import unlink
from os.path import basename


class BorrarArchivoCommand(sublime_plugin.TextCommand):
    def run(self, edit, text_input):
        if not text_input == 'NO': 
            active = self.view.window().active_view()
            unlink(active.file_name())
            active.close()
        
    def input(self, args):
        return TestTextInputHandler(self.view)
 

class TestTextInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view
        self.file = self.view.window().active_view().file_name()

    def initial_text(self):
        return 'NO'

    def name(self):
        return 'text_input'

    def preview(self, text):
        return 'Quieres borrar "{}"'.format(basename(self.file))