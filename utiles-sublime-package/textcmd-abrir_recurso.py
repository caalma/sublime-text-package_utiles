import sublime
import sublime_plugin
import webbrowser
from os.path import exists, realpath, dirname, join, expanduser

class AbrirRecursoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        err = []
        for region in self.view.sel():
            start = region.a
            end = region.b

            view_size = self.view.size()
            terminator = ['\t', ' ', '\"', '\'', '(', ')']

            while (start > 0
                    and not self.view.substr(start - 1) in terminator
                    and self.view.classify(start) & sublime.CLASS_LINE_START == 0):
                start -= 1

            while (end < view_size
                    and not self.view.substr(end) in terminator
                    and self.view.classify(end) & sublime.CLASS_LINE_END == 0):
                end += 1

            path = self.view.substr(sublime.Region(start, end))
            
            if path.startswith('http'):
                webbrowser.open_new_tab(path)
            else:
                file = self.view.window().active_view().file_name()
                folder = dirname(file) if file else expanduser('~')
                uri = realpath(path) if path.startswith('/') else realpath(join(folder, path))

                if exists(uri):
                    webbrowser.open(uri)
                else:
                    err.append(uri)
        if err:
            sublime.status_message('ERROR EN: ' + ', '.join(err))