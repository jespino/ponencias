import gtk

def boton_clickeado(widget):
	print "hola mundo"

window = gtk.Window()

button = gtk.Button()
button.show()
window.add(button)
button.set_label("Pulse Aqui")
button.connect("clicked",boton_clickeado)

window.show()

gtk.main()
