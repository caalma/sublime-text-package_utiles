import sublime
import sublime_plugin
from os.path import dirname, expanduser
from subprocess import Popen, PIPE
from datetime import datetime
from os import unlink


if 'linux' == sublime.platform():
    disponible = True
    cmd_python = 'python3'

if 'windows' == sublime.platform():
    disponible = False
    cmd_python = 'python'


class CmdBashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if disponible:
            se = '\n'
            te = '!!!'
            to = ''
            prefijo_ignorar_respuesta = '!'
            ignorar_respuesta = False

            for region in self.view.sel():
                res = []
                cmd = self.view.substr(region).strip()
                if cmd[0] == prefijo_ignorar_respuesta:
                    cmd = cmd[1:]
                    ignorar_respuesta = True 

                art = self.view.window().active_view().file_name()
                ruta = dirname(art) if art else expanduser('~')
                
                process = Popen(['bash', '-c', cmd], shell=False, cwd=ruta, stdout=PIPE, stderr=PIPE)

                if ignorar_respuesta:
                    res = ''
                else:
                    out = process.stdout.read().decode('utf8')
                    err = process.stderr.read().decode('utf8')

                    if len(out) > 0:
                        if len(out) == 0:
                            res.append('')  
                        else:
                            res.append(to + se + out)  

                    if len(err) > 0:
                        res.append(te + se + err)  
                
                self.view.insert(edit, region.end(), se.join(res))


class CmdPython3Command(sublime_plugin.TextCommand):
    def run(self, edit):
        if disponible:
            se = '\n'
            te = '!!!'
            to = ''
            prefijo_ignorar_respuesta = '!'
            ignorar_respuesta = False

            for region in self.view.sel():
                res = []

                cmd = self.view.substr(region).strip()
                if cmd[0] == prefijo_ignorar_respuesta:
                    cmd = cmd[1:]
                    ignorar_respuesta = True 

                art = self.view.window().active_view().file_name()
                ruta = dirname(art) if art else expanduser('~')
                artmp = '{}/tmp_{}'.format(ruta, int(datetime.now().timestamp()))

                with open(artmp, 'w') as f:
                    f.write(cmd)
                
                process = Popen([cmd_python, artmp], shell=False, cwd=ruta, stdout=PIPE, stderr=PIPE)

                if ignorar_respuesta:
                    res = ''
                else:
                    out = process.stdout.read().decode('utf8')
                    err = process.stderr.read().decode('utf8')
                    
                    if len(out) > 0:
                        if len(out) == 0:
                            res.append('')  
                        else:
                            res.append(to + se + out)  
                            
                    if len(err) > 0:
                        res.append(te + se + err)  
                
                self.view.insert(edit, region.end(), se.join(res))
                unlink(artmp)

class CmdNodejsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if disponible:
            se = '\n'
            te = '!!!'
            to = ''
            prefijo_ignorar_respuesta = '!'
            ignorar_respuesta = False
        
            for region in self.view.sel():
                res = []
                cmd = self.view.substr(region).strip()
                if cmd[0] == prefijo_ignorar_respuesta:
                    cmd = cmd[1:]
                    ignorar_respuesta = True 

                art = self.view.window().active_view().file_name()
                ruta = dirname(art) if art else expanduser('~')
                artmp = '{}/tmp_{}'.format(ruta, int(datetime.now().timestamp()))

                with open(artmp, 'w') as f:
                    f.write(cmd)
                
                process = Popen(['nodejs', artmp], shell=False, cwd=ruta, stdout=PIPE, stderr=PIPE)

                if ignorar_respuesta:
                    res = ''
                else:
                    out = process.stdout.read().decode('utf8')
                    err = process.stderr.read().decode('utf8')
                    
                    if len(out) > 0:
                        if len(out) == 0:
                            res.append('')  
                        else:
                            res.append(to + se + out)  
                            
                    if len(err) > 0:
                        res.append(te + se + err)  
                
                self.view.insert(edit, region.end(), se.join(res))
                unlink(artmp)