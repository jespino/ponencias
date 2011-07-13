import gtk
import webkit

def load_url(widget):
	wk.open(entry.get_text())

window = gtk.Window()
wk = webkit.WebView()
vbox = gtk.VBox()
hbox = gtk.HBox()
entry = gtk.Entry()
button = gtk.Button()
button.set_label("Ir")

hbox.add(entry)
hbox.add(button)

vbox.add(hbox)
vbox.add(wk)

window.add(vbox)
window.show_all()

button.connect("clicked",load_url)
window.connect("destroy",gtk.main_quit)

gtk.main()
