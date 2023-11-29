class Actividad:
    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Tarea : {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}"

    def realizar_tarea(self):
        print(f"Realizando la tarea: {self.titulo}")


class ActividadDiaria(Actividad):
    def __init__(self, titulo, descripcion, estado, prioridad):
        super().__init__(titulo, descripcion, estado)
        self.prioridad = prioridad

    def realizar_tarea(self):
        print(f"Realizando la tarea casual: {self.titulo} (Prioridad: {self.prioridad})")


class ActividadImportante(Actividad):
    def __init__(self, titulo, descripcion, estado, fecha_limite):
        super().__init__(titulo, descripcion, estado)
        self.fecha_limite = fecha_limite

    def realizar_tarea(self):
        print(f"Realizando la tarea importante: {self.titulo} (Fecha límite: {self.fecha_limite})")


class Actividadtarea(Actividad):
    def __init__(self, titulo, descripcion, estado, periodicidad):
        super().__init__(titulo, descripcion, estado)
        self.periodicidad = periodicidad

    def realizar_tarea(self):
        print(f"Realizando la tarea diaria: {self.titulo} (Periodicidad: {self.periodicidad})")


# Ejemplo de uso del polimorfismo
tarea_casual = ActividadDiaria("Comprar café", "Ir al supermercado", "Pendiente", "Alta")
tarea_importante = ActividadImportante("Preparar presentación", "Preparar diapositivas", "Pendiente", "2023-12-01")
tarea_diario = Actividadtarea("Hacer ejercicio", "Ir al gimnasio", "Pendiente", "Diaria")

# Realizar tareas de manera uniforme a través de la clase base
tareas = [tarea_casual, tarea_importante, tarea_diario]
for tarea in tareas:
    print(tarea)
    tarea.realizar_tarea()
    print("\n")
