import signal
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import requests
import time

UUID='testcoll'
URL='http://127.0.0.1:5000'


builder = Gtk.Builder()
builder.add_from_file('simple.glade')
#builder.connect_signals(Handler())

window = builder.get_object('window')
window.set_icon_from_file('python3.xpm')
lgen = locals()
for i in range(1,4):
    lgen[f'entry{i}'] = builder.get_object(f'entry{i}')
menu1 = builder.get_object('menu1')
button1 = builder.get_object('button1')
spinner1 = builder.get_object('spinner1')
labelT = builder.get_object('labelT')

spinner1.activate()
spinner1.start()


def send(button1):
    headers = dict(Water=str(entry1.get_text()),Electric=str(entry2.get_text()),Gas=str(entry3.get_text()))
    labelT.set_text(str(headers))
    spinner1.stop()
    return requests.post(f'{URL}/add/{UUID}', headers=headers)


button1.connect('clicked', send)
#icon = TrayIcon(APPID, ICON, menu)
#Notify.init(APPID)

window.show_all()
Gtk.main()
