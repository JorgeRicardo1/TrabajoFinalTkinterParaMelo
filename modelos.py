class Tarea:
    def __init__(self, tarea_id, titulo, descripcion, estado):
        self.tarea_id = tarea_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Tarea {self.tarea_id}: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}"

    def realizar_tarea(self):
        print(f"Realizando la tarea: {self.titulo}")


class TareaCasual(Tarea):
    def __init__(self, tarea_id, titulo, descripcion, estado, prioridad):
        super().__init__(tarea_id, titulo, descripcion, estado)
        self.prioridad = prioridad

    def realizar_tarea(self):
        print(f"Realizando la tarea casual: {self.titulo} (Prioridad: {self.prioridad})")


class TareaImportante(Tarea):
    def __init__(self, tarea_id, titulo, descripcion, estado, fecha_limite):
        super().__init__(tarea_id, titulo, descripcion, estado)
        self.fecha_limite = fecha_limite

    def realizar_tarea(self):
        print(f"Realizando la tarea importante: {self.titulo} (Fecha límite: {self.fecha_limite})")


class TareaDiario(Tarea):
    def __init__(self, tarea_id, titulo, descripcion, estado, periodicidad):
        super().__init__(tarea_id, titulo, descripcion, estado)
        self.periodicidad = periodicidad

    def realizar_tarea(self):
        print(f"Realizando la tarea diaria: {self.titulo} (Periodicidad: {self.periodicidad})")


# Ejemplo de uso del polimorfismo
tarea_casual = TareaCasual(1, "Comprar café", "Ir al supermercado", "Pendiente", "Alta")
tarea_importante = TareaImportante(2, "Preparar presentación", "Preparar diapositivas", "Pendiente", "2023-12-01")
tarea_diario = TareaDiario(3, "Hacer ejercicio", "Ir al gimnasio", "Pendiente", "Diaria")

# Realizar tareas de manera uniforme a través de la clase base
tareas = [tarea_casual, tarea_importante, tarea_diario]
for tarea in tareas:
    print(tarea)
    tarea.realizar_tarea()
    print("\n")
