from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

#COLORES
fondoContendio = "#D5CABD" 

#VARIABLES
tituloCabecera = "Mi dia"
tipo_selected = ""
lista = []


def mostrar_seccion(seccion):
    # Oculta todas las secciones
    cabeceraContenidoFrame.grid(row=0, column=1, sticky="nswe")
    seccionContenidoFrame.grid(row=1, column=1, sticky="nsew")
    for frame in secciones_contenido:
        frame.grid_forget()
    # Muestra la sección deseada
    secciones_contenido[seccion].grid(row=1, column=1, sticky="nsew")
    if seccion == 0:
        tituloCabecera = "Mi dia"
    elif seccion == 1:
        tituloCabecera = "Importante"
    elif seccion == 2:
        tituloCabecera = "Tareas"
    else:
        tituloCabecera = ""
        cabeceraContenidoFrame.grid_forget()
        seccionContenidoFrame.grid(row=0, column=1,rowspan=2, sticky="nsew")
    titleCabeceraLabel.config(text=tituloCabecera)

def hover_btn_enter(event):
    if event.widget.cget('text') != 'Añadir':
        event.widget.config(bg='gray')  # Cambiar color de fondo al pasar el ratón
    else:
        event.widget.config(bg='#ADD19D')

def hover_btn_leave(event):
    if event.widget.cget('text') != 'Añadir':
        event.widget.config(bg='#F0F0F0')  # Cambiar color de fondo al pasar el ratón
    else:
        event.widget.config(bg='#85BA6D')

def on_checkbox_select(var, tipoSeleccionada):
    if tipoSeleccionada == "diaria" and var.get() == 1:
        nuevoClaseImportanteCheckBtn.deselect()
        nuevoClaseTareaCheckBtn.deselect()
        nuevoEspecialLabel.config(text="Importancia:")
        tareaSelectedChBox.set = 0
        importanteSelectedChBox.set = 0
    elif tipoSeleccionada == "importante" and var.get() == 1:
        nuevoClaseDiariaCheckBtn.deselect()
        nuevoClaseTareaCheckBtn.deselect()
        nuevoEspecialLabel.config(text="Fecha Limite:")
        diariaSelectedChBox.set = 0
        tareaSelectedChBox.set = 0
    elif tipoSeleccionada == "tarea" and var.get() == 1:
        nuevoClaseDiariaCheckBtn.deselect()
        nuevoClaseImportanteCheckBtn.deselect()
        nuevoEspecialLabel.config(text="Frecuencia:")
        diariaSelectedChBox.set = 0
        importanteSelectedChBox.set = 0

def add_new_task():
    guardarTitulo = tituloVar.get()
    guardarDescripcion = descripcionVar.get()
    guardarEspecial = espcialVar.get()

    if diariaSelectedChBox.get() == 1:
        guardarTipo = "diaria"
    elif importanteSelectedChBox.get() == 1:
        guardarTipo = "importante"
    elif tareaSelectedChBox.get() == 1:
        guardarTipo = "tarea"
    
    lista.append(guardarTitulo + "$" + guardarDescripcion + "$" + guardarEspecial + "$" +  guardarTipo)
    escribirContacto()
    messagebox.showinfo("Guardado", "El contacto ha sido guardado en la agenda")
    tituloVar.set("")
    descripcionVar.set("")
    espcialVar.set("")
    diariaSelectedChBox.set = 0
    importanteSelectedChBox.set = 0
    tareaSelectedChBox.set = 0
    consultar()

def escribirContacto():
    archivo = open("bd.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento + "\n")
    archivo.close()

def consultar():
    print(lista)


ventanaPrincipal = Tk()
ventanaPrincipal.title = "App To Do"
ventanaPrincipal.geometry("800x400")
#variables
diariaSelectedChBox = IntVar()
importanteSelectedChBox = IntVar()
tareaSelectedChBox = IntVar()

tituloVar = StringVar()
descripcionVar = StringVar()
estadoVar = StringVar()
espcialVar = StringVar()


#--- configuracion grid-------
ventanaPrincipal.columnconfigure(0, weight=2)
ventanaPrincipal.columnconfigure(1, weight=8)

ventanaPrincipal.rowconfigure(0, weight=2)
ventanaPrincipal.rowconfigure(1, weight=8)

#region --------------Inicio Menu lateral------------------
menuLateralFrame = Frame(ventanaPrincipal, bd=2, relief="solid")
menuLateralFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

menuLateralFrame.rowconfigure(0, weight=1)
menuLateralFrame.rowconfigure(1, weight=9)

menuLateralFrame.columnconfigure(0, weight=1)

titleMenuLateralLabel = Label(menuLateralFrame, text="Proyectos to do", font=("Arial", 16))
titleMenuLateralLabel.grid(row=0, column=0, columnspan=2)

#region --Contenedor botones---
contendorBotonesFrame = Frame(menuLateralFrame)
contendorBotonesFrame.grid(row=1, column=0, sticky="new")

contendorBotonesFrame.columnconfigure(0, weight=2)
contendorBotonesFrame.columnconfigure(1, weight=8)

miDiaBtn = Button(contendorBotonesFrame, text="Mi dia",
                  relief=FLAT)
miDiaBtn.grid(row=0, column=1, sticky="nsew", pady=10)
miDiaBtn.bind('<Enter>', hover_btn_enter)
miDiaBtn.bind('<Leave>', hover_btn_leave)

importanteBtn = Button(contendorBotonesFrame, text="Importante",
                       relief=FLAT)
importanteBtn.grid(row=1, column=1, sticky="nsew", pady=10)
importanteBtn.bind('<Enter>', hover_btn_enter)
importanteBtn.bind('<Leave>', hover_btn_leave)

tareasBtn = Button(contendorBotonesFrame, text="Tareas",relief=FLAT)
tareasBtn.grid(row=2, column=1, sticky="nsew", pady=10)
tareasBtn.bind('<Enter>', hover_btn_enter)
tareasBtn.bind('<Leave>', hover_btn_leave)

agregarBtn = Button(contendorBotonesFrame, text="Añadir", relief=FLAT, bg="#85BA6D")
agregarBtn.grid(row=3, column=0, columnspan=2, sticky="nswe", pady=10)
agregarBtn.bind('<Enter>', hover_btn_enter)
agregarBtn.bind('<Leave>', hover_btn_leave)

miDiaImg = Image.open("./international-day.png")
miDiaImg = miDiaImg.resize((24,24), Image.ADAPTIVE)
miDiaImgReSize = ImageTk.PhotoImage(miDiaImg)
miDiaImgLabel = Label(contendorBotonesFrame, image=miDiaImgReSize)
miDiaImgLabel.grid(row=0, column=0, sticky="nswe", pady=10)

estrellaImg = Image.open("./estrella2.png")
estrellaImg = estrellaImg.resize((24,24), Image.ADAPTIVE)
estrellaImgReSize = ImageTk.PhotoImage(estrellaImg)
estrellaImgLabel = Label(contendorBotonesFrame,image=estrellaImgReSize)
estrellaImgLabel.grid(row=1,column=0,  sticky="ewns", pady=10)

equipajeImg = Image.open("./equipaje.png")
equipajeImg = equipajeImg.resize((24,24), Image.ADAPTIVE)
equipajeImgReSize = ImageTk.PhotoImage(equipajeImg)
equipajeImgLabel = Label(contendorBotonesFrame, image=equipajeImgReSize)
equipajeImgLabel.grid(row=2, column=0, sticky="nswe", pady=10)

#endregion -- Fin Contenedor botones---

#endregion --------------Fin Menu lateral------------------

# region -------------- Inicio Cabecera seccion contenido ----
cabeceraContenidoFrame = Frame(ventanaPrincipal, bg="#83a300")
cabeceraContenidoFrame.grid(row=0, column=1, sticky="nsew")
titleCabeceraLabel = Label(cabeceraContenidoFrame, text=tituloCabecera, font=("Arial", 16),
                           bg="#83a300")
titleCabeceraLabel.pack(anchor=W)

#endregion -------------- fin Cabecera seccion contenido ----

# region ----------- Inicio Seccion contenido----------------
seccionContenidoFrame = Frame(ventanaPrincipal, bg=fondoContendio)
seccionContenidoFrame.grid(row=1, column=1, sticky="nsew")



# endregion----------- End Content Section----------------

# region------- Crear secciones de contenido
seccion_mi_dia = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_mi_dia.grid(row=1, column=1, sticky="nsew")
Label(seccion_mi_dia, text="Contenido de Mi Día", font=("Arial", 14), bg=fondoContendio).pack()

seccion_importante = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_importante.grid(row=1, column=1, sticky="nsew")
Label(seccion_importante, text="Contenido de Importante", font=("Arial", 14), bg=fondoContendio).pack()

seccion_tareas = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_tareas.grid(row=1, column=1, sticky="nsew")
Label(seccion_tareas, text="Contenido de Tareas", font=("Arial", 14), bg=fondoContendio).pack()

seccion_agregar = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_agregar.grid(row=0, column=1, sticky="nsew")
#region --Seccion agregar inicio --
titleSeccionAgregar = Label(seccion_agregar, text="Añadiendo nueva tarea", font=("Arial", 14), bg=fondoContendio)
titleSeccionAgregar.grid(row=0,column=0)

nuevoTituloLabel = Label(seccion_agregar, text="Título:")
nuevoTituloLabel.grid(row=1, column=0)
nuevoTituloEntry = Entry(seccion_agregar, textvariable=tituloVar)
nuevoTituloEntry.grid(row=1, column=1, columnspan=3, sticky="ew")

nuevoDescripciomLabel = Label(seccion_agregar, text="Descripcion:")
nuevoDescripciomLabel.grid(row=2, column=0)
nuevoDescripciomEntry = Entry(seccion_agregar, textvariable=descripcionVar)
nuevoDescripciomEntry.grid(row=2, column=1, columnspan=3, sticky="ew")

tipoLabel = Label(seccion_agregar, text="Tipo:")
tipoLabel.grid(row=3)

nuevoClaseDiariaCheckBtn = Checkbutton(seccion_agregar,  text="Diaria", variable=diariaSelectedChBox,
                                       command=lambda: on_checkbox_select(diariaSelectedChBox, "diaria"))
nuevoClaseDiariaCheckBtn.grid(row=3, column=1)

nuevoClaseImportanteCheckBtn = Checkbutton(seccion_agregar, text="Importante", variable=importanteSelectedChBox,
                                       command=lambda: on_checkbox_select(importanteSelectedChBox, "importante"))
nuevoClaseImportanteCheckBtn.grid(row=3, column=2)

nuevoClaseTareaCheckBtn = Checkbutton(seccion_agregar, text="Tarea", variable=tareaSelectedChBox,
                                       command=lambda: on_checkbox_select(tareaSelectedChBox, "tarea"))
nuevoClaseTareaCheckBtn.grid(row=3, column=3)

nuevoEspecialLabel = Label(seccion_agregar, text="Importancia")
nuevoEspecialLabel.grid(row=5, column=0)
nuevoEspecialEntry = Entry(seccion_agregar, textvariable=espcialVar)
nuevoEspecialEntry.grid(row=5, column=1, columnspan=3, sticky="ew")

nuevoAgregarBtn = Button(seccion_agregar, text="Agregar", command=add_new_task)
nuevoAgregarBtn.grid(row=6, column=1, columnspan=2, sticky="ew")
#endregion --Seccion agregar  --

# Lista de secciones de contenido
secciones_contenido = [seccion_mi_dia, seccion_importante, seccion_tareas, seccion_agregar]

# Asocia cada botón con la función mostrar_seccion y pasa el índice de la sección como argumento
miDiaBtn.config(command=lambda: mostrar_seccion(0))
importanteBtn.config(command=lambda: mostrar_seccion(1))
tareasBtn.config(command=lambda: mostrar_seccion(2))
agregarBtn.config(command=lambda: mostrar_seccion(3))

# endregion------- Crear secciones de contenido

# Inicialmente, muestra la sección de Mi Día
mostrar_seccion(0)
# Crear un estilo


ventanaPrincipal.mainloop()

