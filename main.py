class RescateDatosCriticos:
    def __init__(self):
        self.tareas = {
            'A': {'desc': 'Identificar servidores afectados', 'duracion': 15, 'dep': []},
            'B': {'desc': 'Priorizar datos críticos', 'duracion': 20, 'dep': ['A']},
            'C': {'desc': 'Activar protocolo de recuperación', 'duracion': 10, 'dep': ['A']},
            'D': {'desc': 'Asignar técnicos a servidores', 'duracion': 5, 'dep': ['C']},
            'E': {'desc': 'Recuperar datos de servidor 1', 'duracion': 30, 'dep': ['B', 'D']},
            'F': {'desc': 'Recuperar datos de servidor 2', 'duracion': 25, 'dep': ['B', 'D']},
            'G': {'desc': 'Validar integridad de datos recuperados', 'duracion': 15, 'dep': ['E', 'F']},
            'H': {'desc': 'Generar informe preliminar para dirección', 'duracion': 10, 'dep': ['G']},
            'I': {'desc': 'Comunicar a clientes afectados', 'duracion': 20, 'dep': ['G']},
            'J': {'desc': 'Coordinar con equipo legal', 'duracion': 15, 'dep': ['G']},
            'K': {'desc': 'Preparar plan de contingencia', 'duracion': 25, 'dep': ['G']}
        }
        self.tiempo_total = 120  # minutos

    def objetivo_proyecto(self):
        return ("Rescatar los datos médicos más críticos en 120 minutos, "
                "minimizando la pérdida de información y comunicando a todas las partes interesadas.")

    def diagrama_flujo(self):
        print("Diagrama de flujo (tareas y dependencias):")
        for clave, tarea in self.tareas.items():
            print(f"{clave}: {tarea['desc']} (depende de: {', '.join(tarea['dep']) or 'ninguna'})")

    def nivelacion_recursos(self):
        print("Nivelación de recursos: Asignar técnicos y herramientas según dependencias y tareas en paralelo.")
        print("- Técnicos asignados tras protocolo de recuperación (D).")
        print("- Recuperación de datos de servidores 1 y 2 puede hacerse en paralelo (E, F).")
        print("- Validación y comunicaciones se pueden solapar tras recuperación (G, H, I, J, K).")

    def plan_comunicacion(self):
        print("Plan de comunicación de crisis:")
        print("- Informar a dirección tras validación de datos (H).")
        print("- Comunicar a clientes afectados tras validación (I).")
        print("- Coordinar con equipo legal tras validación (J).")
        print("- Preparar plan de contingencia tras validación (K).")

    def mostrar_cronograma(self):
        print("Cronograma estimado de tareas:")
        for clave, tarea in self.tareas.items():
            print(f"{clave}: {tarea['desc']} - {tarea['duracion']} min")

if __name__ == "__main__":
    rescate = RescateDatosCriticos()
    print("🧠 Reto de Algoritmos: Rescate de Datos Críticos en una Infraestructura Comprometida\n")
    print("Objetivo del Proyecto:")
    print(rescate.objetivo_proyecto())
    print("\n---")
    rescate.diagrama_flujo()
    print("\n---")
    rescate.nivelacion_recursos()
    print("\n---")
    rescate.plan_comunicacion()
    print("\n---")
    rescate.mostrar_cronograma()