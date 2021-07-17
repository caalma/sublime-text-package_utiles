# -*- coding:utf8 -*- 

import sublime
import sublime_plugin


class TestCommand(sublime_plugin.TextCommand):
    def run(self, edit, text_input):
        for region in self.view.sel():
            
            text_extra = 'TEST'
            text = ' # {} {} {}'.format(text_extra, text_input)

            self.view.insert(edit, region.end(), text)
 
            sublime.status_message(text)
            if sublime.ok_cancel_dialog('Esto es una prueba?', 'SI', 'NO'):
                sublime.message_dialog('BIEN: ' + text)
            else:
                sublime.error_message('ERROR: ' + text)

    def input(self, args):
        return TestTextInputHandler(self.view)

 
class TestTextInputHandler(sublime_plugin.TextInputHandler):
    def __init__(self, view):
        self.view = view

    def name(self):
        return "text_input"

    def placeholder(self):
        return "Texto a insertar"

    def preview(self, text):
        return ("Selections: {}, Characters: {}"
                .format(len(self.view.sel()), len(text)))