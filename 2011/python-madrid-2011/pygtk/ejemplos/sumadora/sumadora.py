import gtk
from gtk import Builder

def gtk_main_quit(widget):
	gtk.main_quit()

def plus_clicked(widget):
	entry1 = builder.get_object("entry1")
	entry2 = builder.get_object("entry2")
	entry3 = builder.get_object("entry3")
	label1 = builder.get_object("label1")

	label1.set_text(str(int(entry1.get_text())+int(entry2.get_text())+int(entry3.get_text())))

builder = Builder()
builder.add_from_file("sumadora.glade")
builder.connect_signals(locals())
window = builder.get_object("window1")
window.show()

gtk.main()
