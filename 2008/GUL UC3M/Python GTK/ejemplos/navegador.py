import gtk
import gtkmozembed

def gtk_main_quit(widget):
	gtk.main_quit()

def load_url(widget):
	moz.load_url(entry.get_text())

window = gtk.Window()
moz = gtkmozembed.MozEmbed()
vbox = gtk.VBox()
hbox = gtk.HBox()
entry = gtk.Entry()
button = gtk.Button()
button.set_label("Ir")

hbox.add(entry)
hbox.add(button)

vbox.add(hbox)
vbox.add(moz)

window.add(vbox)
window.show_all()

button.connect("clicked",load_url)
window.connect("destroy",gtk_main_quit)

gtk.main()
