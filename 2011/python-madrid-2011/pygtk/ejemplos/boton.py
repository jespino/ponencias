import gtk

def boton_clickeado(widget):
	widget.set_label("hola mundo")

window = gtk.Window()

button = gtk.Button()
button.show()
window.add(button)
button.set_label("Pulse Aqui")
button.connect("clicked",boton_clickeado)
window.connect("destroy",gtk.main_quit)

window.show()

gtk.main()
