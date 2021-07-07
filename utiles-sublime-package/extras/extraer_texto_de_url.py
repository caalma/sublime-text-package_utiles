#!/usr/bin/python3
# -*- coding:utf8 -*-

from sys import argv
from pyquery import PyQuery

def extraer(url):
    dom = PyQuery(url=url)
    dom.find('script').remove()
    dom.find('link').remove()
    dom.find('style').remove()
    dom.find('meta').remove()

    urls = []
    
    tt = dom.find('img')
    for t in tt:
    	e = PyQuery(t)
    	e.text('({})[*{}]'.format(e.attr('alt'), len(urls)+1))
    	urls.append(e.attr('src'))

    tt = dom.find('a')
    for t in tt:
    	e = PyQuery(t)
    	e.text('«{}»[*{}]'.format(e.text(), len(urls)+1))
    	urls.append(e.attr('href'))

    tt = dom.find('h1')
    for t in tt:
        e = PyQuery(t)
        e.text('\n\n# {}\n\n'.format(e.text()))

    tt = dom.find('h2')
    for t in tt:
        e = PyQuery(t)
        e.text('\n\n## {}\n\n'.format(e.text()))

    tt = dom.find('p')
    for t in tt:
        e = PyQuery(t)
        e.text('{}\n\n'.format(e.text()))

    tt = dom.find('li')
    for t in tt:
        e = PyQuery(t)
        e.text('+ {}\n'.format(e.text()))

    tex = dom.text()

    tex += '\n------------ Lista de URLs\n' + '\n'.join(['[*{}] > {}'.format(i+1, v) for i, v  in enumerate(urls)])
    return '\n\n\n'+tex

if __name__ == '__main__':	
    r = extraer(argv[1])
    print(r)
    exit()