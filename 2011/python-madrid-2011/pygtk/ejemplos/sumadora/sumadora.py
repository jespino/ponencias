import gtk
from gtk import Builder

def gtk_main_quit(widget):
	gtk.main_quit()

def plus_clicked(widget):
	entry1 = xml.get_widget("entry1")
	entry2 = xml.get_widget("entry2")
	label1 = xml.get_widget("label1")

	label1.set_text(str(int(entry1.get_text())+int(entry2.get_text())))

builder = Builder()
builder.add_from_file("sumadora.glade")
builder.signal_autoconnect(locals())

gtk.main()
