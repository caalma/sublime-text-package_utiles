import sublime
import sublime_plugin


class NormalizeCommand(sublime_plugin.TextCommand):
    SIGNS_TO_REPLACE = [
        ['ñ', 'nn'],
        ['á', 'a'],
        ['é', 'e'],
        ['í', 'i'],
        ['ó', 'o'],
        ['ú', 'u'],
    ]
    SIGNS_ALLOWED = 'abcdefghijklmnopqrstuvwxyz1234567890._'
    SIGN_FORN_NOT_ALLOWED = '_'

    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            t = self.view.substr(region)
            self.view.replace(edit, region, self.adjust(t))

    def replace(self, t):
        for r in self.SIGNS_TO_REPLACE:
            t = t.replace(r[0], r[1])
        return t
        
    def allowed(self, t):
        r = []
        for s in t:
            if not s in self.SIGNS_ALLOWED:
                s = self.SIGN_FORN_NOT_ALLOWED
            r.append(s)
        return ''.join(r)

    def adjust(self, t):
        t = t.lower()
        t = self.replace(t)
        t = self.allowed(t)
        return t