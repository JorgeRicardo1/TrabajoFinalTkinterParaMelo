from tkinter import *
import time

ventanaPrincipal = Tk()
ventanaPrincipal.title = "App To Do"
ventanaPrincipal.geometry("800x400")
#--- configuracion grid-------
ventanaPrincipal.columnconfigure(0, weight=2)
ventanaPrincipal.columnconfigure(1, weight=8)

ventanaPrincipal.rowconfigure(0, weight=2)
ventanaPrincipal.rowconfigure(1, weight=8)

#--------------Inicio Menu lateral------------------
menuLateralFrame = Frame(ventanaPrincipal, bd=2, relief="solid")
menuLateralFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

menuLateralFrame.rowconfigure(0, weight=1)
menuLateralFrame.rowconfigure(1, weight=9)

menuLateralFrame.columnconfigure(0, weight=1)

titleMenuLateralLabel = Label(menuLateralFrame, text="Proyectos to do", font=("Arial", 16))
titleMenuLateralLabel.grid(row=0, column=0, columnspan=2)

#--Contenedor botones--
contendorBotonesFrame = Frame(menuLateralFrame, bg="red")
contendorBotonesFrame.grid(row=1, column=0, sticky="nsew")

contendorBotonesFrame.columnconfigure(0, weight=2)
contendorBotonesFrame.columnconfigure(1, weight=8)

miDia = Button(contendorBotonesFrame, text="Mi dia")
miDia.grid(row=0, column=0)

importanteBtn = Button(contendorBotonesFrame, text="Importante")
importanteBtn.grid(row=1, column=1)

tareasBtn = Button(contendorBotonesFrame, text="Tareas")
tareasBtn.grid(row=2, column=1)


#--------------Fin Menu lateral------------------

#-------------- Inicio Cabecera seccion contenido ----
cabeceraContenidoFrame = Frame(ventanaPrincipal, bg="#83a300")
cabeceraContenidoFrame.grid(row=0, column=1, sticky="nsew")
titleCabeceraLabel = Label(cabeceraContenidoFrame, text="My Day", font=("Arial", 16),
                           bg="#83a300")
titleCabeceraLabel.pack(anchor=W)

#----------------- Fin Cabecera seccion contenido ----

#----------- Inicio Seccion contenido----------------
seccionContenidoFrame = Frame(ventanaPrincipal, bg="#bac9a9")
seccionContenidoFrame.grid(row=1, column=1, sticky="nsew")

#----------- End Content Section----------------


ventanaPrincipal.mainloop()