import sublime
import sublime_plugin


class NormalizarCommand(sublime_plugin.TextCommand):
    SIGNOS_A_REEMPLAZAR = [
        ['ñ', 'nn'],
        ['á', 'a'],
        ['é', 'e'],
        ['í', 'i'],
        ['ó', 'o'],
        ['ú', 'u'],
    ]
    SIGNOS_A_PERMITIDOS = 'abcdefghijklmnopqrstuvwxyz1234567890._'
    SIGNO_PARA_NO_PERMITIDOS = '_'

    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            t = self.view.substr(region)
            self.view.replace(edit, region, self.ajustar(t))

    def caja(self, t):
        return t.lower()

    def reemplazos(self, t):
        for r in self.SIGNOS_A_REEMPLAZAR:
            t = t.replace(r[0], r[1])
        return t
        
    def permitidos(self, t):
        r = []
        for s in t:
            if not s in self.SIGNOS_A_PERMITIDOS:
                s = self.SIGNO_PARA_NO_PERMITIDOS
            r.append(s)
        return ''.join(r)

    def ajustar(self, t):
        t = self.caja(t)
        t = self.reemplazos(t)
        t = self.permitidos(t)
        return t