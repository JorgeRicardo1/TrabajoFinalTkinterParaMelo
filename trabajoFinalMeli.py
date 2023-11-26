from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

#COLORES
fondoContendio = "#D5CABD" 

#VARIABLES
tituloCabecera = "Mi dia"
tipo_selected = ""
actividadesList = []
actividadesDiariasList = []
actividadesImportantesList = []
actividadesTareasList = []


def mostrar_seccion(seccion, nombre):
    # Oculta todas las secciones
    cabeceraContenidoFrame.grid(row=0, column=1, sticky="nswe")
    seccionContenidoFrame.grid(row=1, column=1, sticky="nsew")
    for frame in secciones_contenido:
        frame.grid_forget()
    # Muestra la sección deseada
    secciones_contenido[seccion].grid(row=1, column=1, sticky="nsew")
    if seccion == 0:
        tituloCabecera = "Mi dia"
        actualizarLista(actividadesDiariasList, second_frameDiaria, 'prioridad:')
    elif seccion == 1:
        tituloCabecera = "Importante"
        actualizarLista(actividadesImportantesList, second_frameImportante, 'fecha limite:') 
    elif seccion == 2:
        tituloCabecera = "Tareas"
        actualizarLista(actividadesTareasList, second_frameTareas, 'frecuencia:') 
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
    
    actividadesList.append(guardarTitulo + "$" + guardarDescripcion + "$" + guardarEspecial + "$" +  guardarTipo)
    escribirActividad()
    messagebox.showinfo("Guardado", "El contacto ha sido guardado en la agenda")
    tituloVar.set("")
    descripcionVar.set("")
    espcialVar.set("")
    diariaSelectedChBox.set = 0
    importanteSelectedChBox.set = 0
    tareaSelectedChBox.set = 0
    consultar()

def consultar():
    actividadesDiariasList.clear()
    actividadesImportantesList.clear()
    actividadesTareasList.clear()
    for actividad in actividadesList:
        arreglo = actividad.split("$")
        if arreglo[3] == 'diaria':
            actividadesDiariasList.append(arreglo)
        elif arreglo[3] ==  'importante':
            actividadesImportantesList.append(arreglo)
        elif arreglo[3] == 'tarea':
            actividadesTareasList.append(arreglo)

def actualizarLista(listaActual, frame, especial):
    for i, actividad in enumerate(listaActual):
        frame_actividad = Frame(frame, bd=2, relief=GROOVE)
        frame_actividad.grid(row=i, column=0, padx=5, pady=5, sticky="ew")

        frame_actividad.columnconfigure(0, weight=1)
        frame_actividad.columnconfigure(1, weight=2)
        frame_actividad.columnconfigure(2, weight=1)
        frame_actividad.columnconfigure(3, weight=1)

        # Añadir contenido al frame
        tituloActividadLabel = Label(frame_actividad, text=actividad[0], font=("Arial", 12))
        tituloActividadLabel.grid(row=0, column=0)

        descripcionActividadLabel = Label(frame_actividad, text=actividad[1])
        descripcionActividadLabel.grid(row=1, column=0, sticky="ew")
        
        espeDescripLabel = Label(frame_actividad, text=especial)
        espeDescripLabel.grid(row=0, column=2)

        especialActividadLabel = Label(frame_actividad, text=actividad[2])
        especialActividadLabel.grid(row=0, column=3)

        modificarBtn = Button(frame_actividad,text='Actualizar', relief=FLAT, background='green')
        modificarBtn.grid(row=1, column=4)
        modificarBtn.bind("<Button-1>", lambda event, index=i: actualizarActividad(index))

        EliminarBtn = Button(frame_actividad,text='Eliminar', relief=FLAT, background='red')
        EliminarBtn.grid(row=1, column=5)
        EliminarBtn.bind("<Button-1>", lambda event, index=i: borrarActividad(index, listaActual))


def mostrar_descripcion(index):
    print(index)
    #label_descripcion.config(text=f"Descripción: {actividad_seleccionada.descripcion}")

def actualizarActividad(index):
    print(index)

def borrarActividad(index, listaActual):
    print(index)
    eliminado = index
    removido = False
    for elemento in actividadesList:
        arreglo = elemento.split("$")
        if listaActual[index] == arreglo:
            actividadesList.remove(elemento)
            removido = True
    escribirActividad()
    consultar()
    # Destruir todos los widgets en el frame correspondiente
    if listaActual is actividadesDiariasList:
        for widget in second_frameDiaria.winfo_children():
            widget.destroy()
        actualizarLista(actividadesDiariasList, second_frameDiaria, 'prioridad:')
    elif listaActual is actividadesImportantesList:
        for widget in second_frameImportante.winfo_children():
            widget.destroy()
        actualizarLista(actividadesImportantesList, second_frameImportante, 'fecha limite:')
    elif listaActual is actividadesTareasList:
        for widget in second_frameTareas.winfo_children():
            widget.destroy()
        actualizarLista(actividadesTareasList, second_frameTareas, 'frecuencia:')

    

    if removido:
        messagebox.showinfo("Eliminar", "Elemento eliminado ")

#region --funciones para manipular el archivo de texto
def escribirActividad():
    archivo = open("bd.txt", "w")
    actividadesList.sort()
    for elemento in actividadesList:
        archivo.write(elemento + "\n")
    archivo.close()

def cargarActividades():
    archivo = open("bd.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            actividadesList.append(linea)
            linea = archivo.readline()
    archivo.close()


def iniciarArchivo():
    archivo = open("bd.txt", "a")
    archivo.close()
#endregion ---------------------

ventanaPrincipal = Tk()
ventanaPrincipal.title = "App To Do"
ventanaPrincipal.geometry("800x400")

iniciarArchivo()
cargarActividades()
consultar()
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

#region --------------inicio Menu lateral------------------
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

miDiaImg = Image.open("./images/international-day.png")
miDiaImg = miDiaImg.resize((24,24), Image.ADAPTIVE)
miDiaImgReSize = ImageTk.PhotoImage(miDiaImg)
miDiaImgLabel = Label(contendorBotonesFrame, image=miDiaImgReSize)
miDiaImgLabel.grid(row=0, column=0, sticky="nswe", pady=10)

estrellaImg = Image.open("./images/estrella2.png")
estrellaImg = estrellaImg.resize((24,24), Image.ADAPTIVE)
estrellaImgReSize = ImageTk.PhotoImage(estrellaImg)
estrellaImgLabel = Label(contendorBotonesFrame,image=estrellaImgReSize)
estrellaImgLabel.grid(row=1,column=0,  sticky="ewns", pady=10)

equipajeImg = Image.open("./images/equipaje.png")
equipajeImg = equipajeImg.resize((24,24), Image.ADAPTIVE)
equipajeImgReSize = ImageTk.PhotoImage(equipajeImg)
equipajeImgLabel = Label(contendorBotonesFrame, image=equipajeImgReSize)
equipajeImgLabel.grid(row=2, column=0, sticky="nswe", pady=10)

#endregion -- Fin Contenedor botones---

#endregion --------------Fin Menu lateral------------------

# region -------------- inicio Cabecera seccion contenido ----
cabeceraContenidoFrame = Frame(ventanaPrincipal, bg="#83a300")
cabeceraContenidoFrame.grid(row=0, column=1, sticky="nsew")
titleCabeceraLabel = Label(cabeceraContenidoFrame, text=tituloCabecera, font=("Arial", 16),
                           bg="#83a300")
titleCabeceraLabel.pack(anchor=W)

#endregion -------------- fin Cabecera seccion contenido ----

# region ----------- inicio Seccion contenido----------------
seccionContenidoFrame = Frame(ventanaPrincipal, bg=fondoContendio)
seccionContenidoFrame.columnconfigure(1, weight=1)
seccionContenidoFrame.rowconfigure(1, weight=1)
seccionContenidoFrame.grid(row=1, column=1, sticky="nsew")


# endregion----------- End Content Section----------------

# region------- Crear secciones de contenido--

#region -- seccion diaria --
seccion_mi_dia = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_mi_dia.grid(row=1, column=1, sticky="nsew")

#canvas
my_canvasDiaria = Canvas(seccion_mi_dia)
my_canvasDiaria.pack(side=LEFT, fill=BOTH, expand=1)

#Scrollbar
my_scrollbarDiaria = Scrollbar(seccion_mi_dia, orient=VERTICAL, command=my_canvasDiaria.yview)
my_scrollbarDiaria.pack(side=RIGHT, fill=Y)

#Configure the canvas
my_canvasDiaria.configure(yscrollcommand=my_scrollbarDiaria.set)
my_canvasDiaria.bind('<Configure>', lambda e: my_canvasDiaria.configure(scrollregion=my_canvasDiaria.bbox("all")))

#create annother frame
second_frameDiaria = Frame(my_canvasDiaria)
#Add thatr new frame inside the canvas
my_canvasDiaria.create_window((0,0), window=second_frameDiaria, anchor="nw")

#endregion -- end seccion diaria -- 

#region --- seccion importante
seccion_importante = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_importante.grid(row=1, column=1, sticky="nsew")

#canvas
my_canvasImportante = Canvas(seccion_importante)
my_canvasImportante.pack(side=LEFT, fill=BOTH, expand=1)

#Scrollbar
my_scrollbarImportante = Scrollbar(seccion_importante, orient=VERTICAL, command=my_canvasImportante.yview)
my_scrollbarImportante.pack(side=RIGHT, fill=Y)

#Configure the canvas
my_canvasImportante.configure(yscrollcommand=my_scrollbarImportante.set)
my_canvasImportante.bind('<Configure>', lambda e: my_canvasImportante.configure(scrollregion=my_canvasImportante.bbox("all")))

#create annother frame
second_frameImportante = Frame(my_canvasImportante)
#Add thatr new frame inside the canvas
my_canvasImportante.create_window((0,0), window=second_frameImportante, anchor="nw")

#endregion --- end seccion importante 

#region --- seccion Tareas--
seccion_tareas = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_tareas.grid(row=1, column=1, sticky="nsew")

#canvas
my_canvasTareas = Canvas(seccion_tareas)
my_canvasTareas.pack(side=LEFT, fill=BOTH, expand=1)

#Scrollbar
my_scrollbarTareas = Scrollbar(seccion_tareas, orient=VERTICAL, command=my_canvasTareas.yview)
my_scrollbarTareas.pack(side=RIGHT, fill=Y)

#Configure the canvas
my_canvasTareas.configure(yscrollcommand=my_scrollbarTareas.set)
my_canvasTareas.bind('<Configure>', lambda e: my_canvasTareas.configure(scrollregion=my_canvasTareas.bbox("all")))

#create annother frame
second_frameTareas = Frame(my_canvasTareas)
second_frameTareas.columnconfigure(0, weight=1)
#Add thatr new frame inside the canvas
my_canvasTareas.create_window((0,0), window=second_frameTareas, anchor="nw")

#endregion --------

#region --Seccion agregar inicio --
seccion_agregar = Frame(seccionContenidoFrame, bg=fondoContendio)
seccion_agregar.grid(row=0, column=1, sticky="nsew")
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
miDiaBtn.config(command=lambda: mostrar_seccion(0 , "diaria"))
importanteBtn.config(command=lambda: mostrar_seccion(1, "importante"))
tareasBtn.config(command=lambda: mostrar_seccion(2, "tareas"))
agregarBtn.config(command=lambda: mostrar_seccion(3, "agregar"))

# endregion------- Crear secciones de contenido

# Inicialmente, muestra la sección de Mi Día
mostrar_seccion(0, "diaria")
# Crear un estilo


ventanaPrincipal.mainloop()

