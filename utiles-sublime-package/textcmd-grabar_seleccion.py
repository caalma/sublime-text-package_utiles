import sublime
import sublime_plugin
import webbrowser


class GrabarSeleccionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.save_dialog(self.save)

    def save(self, filename):
        region = self.view.sel()[0]
        with open(filename, 'w') as f:
            f.write(self.view.substr(sublime.Region(region.a, region.b)))