#!/usr/bin/python3
# -*- coding:utf8 -*- 

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class ClipboardWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def get_cb_text_html(self):
        cnt = Gdk.Atom.intern('text/html', False)
        t = self.clipboard.wait_for_contents(cnt)
        if t:
            return t.get_data().decode('utf-8')
        else:
            return ''


if __name__ == '__main__':
    app = ClipboardWindow()
    print(app.get_cb_text_html())