import sublime
import sublime_plugin
import webbrowser


class BuscarEnDdgCommand(sublime_plugin.TextCommand):
    def run(self, edit, data=''):
        for region in self.view.sel():
            text_input = self.view.substr(region).strip()
            url = 'http://duckduckgo.com?q={}'.format(text_input.replace(' ', '+'))
            webbrowser.open_new_tab(url)