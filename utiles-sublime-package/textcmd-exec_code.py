
import sublime
import sublime_plugin
from os.path import dirname, expanduser
from subprocess import Popen, PIPE
from datetime import datetime
from os import unlink


interpreters = {
    'linux': {
        'bash': ['bash'],
        'python': ['python3'],
        'javascript': ['node'],
        'clisp': ['clisp'],
        'newlisp': ['newlisp', '<'],
        'sbcl': ['sbcl', '--script'],
        'nim': ['nim', 'c', '--hints:off', '-r'], # falla
    },
    'windows': {
        'python': ['python'],
    }
}

     
# ------------ pruebas
''' javascript
console.log(2 + 2);
'''

''' python
print(22*2)
'''

''' bash
ls
'''

''' newlisp
(println (+ 2 2))
'''

''' clisp
(print (+ 2 2))
'''

''' sbcl
(print (+ 2 2))
'''

''' nim
import strformat
let saludo:string = "Hola"
let calculo:int = 2 + 4
echo &"{saludo}, {calculo}"
'''


class CodeBashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'bash')


class CodePython3Command(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'python')


class CodeJavascriptCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'javascript')


class CodeClispCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'clisp')


class CodeNewlispCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'newlisp')


class CodeSbclCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'sbcl')

class CodeNimCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        exec_code(self, edit, 'nim')


def exec_code(self, edit, interpreter):
    current_os = sublime.platform()
    if current_os in interpreters:
        if interpreter in interpreters[current_os]:
            se = '\n'
            te = '!!!'
            to = ''
            ignore_response_prefix = '!'
            ignore_response = False

            for region in self.view.sel():
                response = []

                code = self.view.substr(region).strip()
                if code.startswith(ignore_response_prefix):
                    code = code[1:]
                    ignore_response = True 

                file = self.view.window().active_view().file_name()
                current_path = dirname(file) if file else expanduser('~')
                file_code_tmp = '{}/code_tmp_{}'.format(current_path, int(datetime.now().timestamp()))

                with open(file_code_tmp, 'w') as f:
                    f.write(code)
                
                current_cmd = interpreters[current_os][interpreter] + [file_code_tmp]
                process = Popen(current_cmd, shell=False, cwd=current_path, stdout=PIPE, stderr=PIPE)

                if ignore_response:
                    response = ''
                else:
                    out = process.stdout.read().decode('utf8')
                    err = process.stderr.read().decode('utf8')
                    
                    if len(out) > 0:
                        if len(out) == 0:
                            response.append('')  
                        else:
                            response.append(to + se + out)  
                            
                    if len(err) > 0:
                        response.append(te + se + err)  
                
                self.view.insert(edit, region.end(), se.join(response))
                unlink(file_code_tmp)
                sublime.status_message('> Ejecutado con {}'.format(interpreter))
        else:
            sublime.status_message('!ERROR: Interprete no disponible.')
    else:
        sublime.status_message('!ERROR: No disponible para {}'.format(sublime.platform()))
