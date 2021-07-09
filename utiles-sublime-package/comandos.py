# -*- coding:utf8 -*- 

import sublime
import sublime_plugin
from os.path import dirname, expanduser
from subprocess import Popen, PIPE
from datetime import datetime
import platform
from os import unlink

if 'Linux' == platform.system():
    disponible = True

if 'Windows' == platform.system():
    disponible = False


class cmdbashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if disponible:
            se = '\n'
            te = '!!!'
            to = ''
            prefijo_ignorar_respuesta = '!'
            ignorar_respuesta = False
            ss = self.view.sel()
        
            for s in ss:
                region = s
                posfin = s.end()
                res = []

                cmd = self.view.substr(region).strip()
                if cmd[0] == prefijo_ignorar_respuesta:
                    cmd = cmd[1:]
                    ignorar_respuesta = True 

                art = self.view.window().active_view().file_name()
                ruta = dirname(art) if art else expanduser('~')
                
                p = Popen(['bash', '-c', cmd], shell=False, cwd=ruta, stdout=PIPE, stderr=PIPE)

                if ignorar_respuesta:
                    res = ''
                else:
                    out = p.stdout.read().decode('utf8')
                    err = p.stderr.read().decode('utf8')

                    if len(out) > 0:
                        if len(out) == 0:
                            res.append('')  
                        else:
                            res.append(to + se + out)  

                    if len(err) > 0:
                        res.append(te + se + err)  
                
                self.view.insert(edit, posfin, se.join(res))


class cmdpython3Command(sublime_plugin.TextCommand):
    def run(self, edit):
        if disponible:
            se = '\n'
            te = '!!!'
            to = ''
            prefijo_ignorar_respuesta = '!'
            ignorar_respuesta = False
            ss = self.view.sel()
        
            for s in ss:
                region = s
                posfin = s.end()
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
                
                p = Popen(['python3', artmp], shell=False, cwd=ruta, stdout=PIPE, stderr=PIPE)

                if ignorar_respuesta:
                    res = ''
                else:
                    out = p.stdout.read().decode('utf8')
                    err = p.stderr.read().decode('utf8')
                    
                    if len(out) > 0:
                        if len(out) == 0:
                            res.append('')  
                        else:
                            res.append(to + se + out)  
                            
                    if len(err) > 0:
                        res.append(te + se + err)  
                
                self.view.insert(edit, posfin, se.join(res))
                unlink(artmp)
