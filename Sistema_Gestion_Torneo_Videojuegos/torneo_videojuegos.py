import statistics

# ============================================================
# PRUEBA - Sistema de Gestión de Torneo de Videojuegos Retro
# ============================================================

# Listas y diccionarios para almacenar los datos del torneo
participantes = []   # Guarda la info de cada jugador
equipos = []         # Guarda los equipos formados
partidas = []        # Guarda el historial de partidas


# ============================================================
# SECCIÓN 1: ENTRADA Y VALIDACIÓN DE DATOS
# ============================================================

def registrar_participante():
    """Registra un nuevo participante con sus datos validados."""

    print("\n--- REGISTRO DE PARTICIPANTE ---")

    # Validar que el nombre no esté vacío
    nombre = input("Ingresa el nombre del participante: ").strip()
    if nombre == "":
        print("Error: El nombre no puede estar vacío.")
        return

    # Validar que la edad esté entre 12 y 70
    try:
        edad = int(input("Ingresa la edad del participante: "))
    except ValueError:
        print("Error: La edad debe ser un número.")
        return

    if edad < 12 or edad > 70:
        print("Error: La edad debe estar entre 12 y 70 años.")
        return

    # Validar que el nivel esté entre 1 y 5
    try:
        nivel = int(input("Ingresa el nivel de experiencia (1 al 5): "))
    except ValueError:
        print("Error: El nivel debe ser un número.")
        return

    if nivel < 1 or nivel > 5:
        print("Error: El nivel debe estar entre 1 y 5.")
        return

    # Guardar el participante como diccionario
    participante = {
        "nombre": nombre,
        "edad": edad,
        "nivel": nivel,
        "en_equipo": False   # Para saber si ya está en un equipo
    }

    participantes.append(participante)
    print(f"\n¡Participante '{nombre}' registrado con éxito!")


# ============================================================
# SECCIÓN 2: GESTIÓN DE PARTICIPANTES Y EQUIPOS
# ============================================================

def mostrar_participantes():
    """Muestra la lista de todos los participantes registrados."""

    print("\n--- LISTA DE PARTICIPANTES ---")

    if len(participantes) == 0:
        print("No hay participantes registrados aún.")
        return

    for i, p in enumerate(participantes):
        estado = "En equipo" if p["en_equipo"] else "Sin equipo"
        print(f"{i + 1}. {p['nombre']} | Edad: {p['edad']} | Nivel: {p['nivel']} | Estado: {estado}")


def formar_equipo():
    """Forma un equipo con 2 jugadores que no estén ya en un equipo."""

    print("\n--- FORMAR EQUIPO ---")

    # Filtrar solo los participantes sin equipo
    disponibles = []
    for p in participantes:
        if p["en_equipo"] == False:
            disponibles.append(p)

    if len(disponibles) < 2:
        print("Error: Se necesitan al menos 2 participantes sin equipo para formar uno.")
        return

    # Mostrar los disponibles
    print("Participantes disponibles:")
    for i, p in enumerate(disponibles):
        print(f"{i + 1}. {p['nombre']} (Nivel {p['nivel']})")

    # Seleccionar jugador 1
    try:
        opcion1 = int(input("Selecciona el número del primer jugador: ")) - 1
        opcion2 = int(input("Selecciona el número del segundo jugador: ")) - 1
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return

    if opcion1 < 0 or opcion1 >= len(disponibles) or opcion2 < 0 or opcion2 >= len(disponibles):
        print("Error: Número de jugador inválido.")
        return

    if opcion1 == opcion2:
        print("Error: Debes seleccionar dos jugadores distintos.")
        return

    # Pedir nombre del equipo
    nombre_equipo = input("Ingresa el nombre del equipo: ").strip()
    if nombre_equipo == "":
        print("Error: El nombre del equipo no puede estar vacío.")
        return

    # Verificar que el nombre del equipo sea único
    for e in equipos:
        if e["nombre"] == nombre_equipo:
            print("Error: Ya existe un equipo con ese nombre.")
            return

    jugador1 = disponibles[opcion1]
    jugador2 = disponibles[opcion2]

    # Crear el equipo
    equipo = {
        "nombre": nombre_equipo,
        "jugador1": jugador1["nombre"],
        "jugador2": jugador2["nombre"],
        "puntos": 0,
        "partidas_jugadas": 0
    }

    equipos.append(equipo)

    # Marcar a los jugadores como "en equipo"
    jugador1["en_equipo"] = True
    jugador2["en_equipo"] = True

    print(f"\n¡Equipo '{nombre_equipo}' formado con {jugador1['nombre']} y {jugador2['nombre']}!")


def mostrar_equipos():
    """Muestra todos los equipos formados con sus integrantes."""

    print("\n--- LISTA DE EQUIPOS ---")

    if len(equipos) == 0:
        print("No hay equipos formados aún.")
        return

    for i, e in enumerate(equipos):
        print(f"{i + 1}. Equipo: {e['nombre']}")
        print(f"   Jugadores: {e['jugador1']} y {e['jugador2']}")
        print(f"   Puntos acumulados: {e['puntos']}")
        print(f"   Partidas jugadas: {e['partidas_jugadas']}")


# ============================================================
# SECCIÓN 3: REGISTRO Y ANÁLISIS DE PARTIDAS
# ============================================================

def registrar_partida():
    """Registra una partida entre dos equipos y asigna puntos al ganador."""

    print("\n--- REGISTRAR PARTIDA ---")

    if len(equipos) < 2:
        print("Error: Se necesitan al menos 2 equipos para jugar una partida.")
        return

    # Mostrar los equipos disponibles
    print("Equipos disponibles:")
    for i, e in enumerate(equipos):
        print(f"{i + 1}. {e['nombre']} ({e['puntos']} puntos)")

    # Seleccionar los dos equipos que jugaron
    try:
        opcion1 = int(input("Selecciona el número del primer equipo: ")) - 1
        opcion2 = int(input("Selecciona el número del segundo equipo: ")) - 1
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return

    if opcion1 < 0 or opcion1 >= len(equipos) or opcion2 < 0 or opcion2 >= len(equipos):
        print("Error: Número de equipo inválido.")
        return

    if opcion1 == opcion2:
        print("Error: Los equipos deben ser distintos.")
        return

    equipo_a = equipos[opcion1]
    equipo_b = equipos[opcion2]

    print(f"\n¿Quién ganó la partida entre '{equipo_a['nombre']}' y '{equipo_b['nombre']}'?")
    print(f"1. {equipo_a['nombre']}")
    print(f"2. {equipo_b['nombre']}")

    try:
        ganador_opcion = int(input("Selecciona el equipo ganador: "))
    except ValueError:
        print("Error: Debes ingresar 1 o 2.")
        return

    if ganador_opcion == 1:
        ganador = equipo_a
    elif ganador_opcion == 2:
        ganador = equipo_b
    else:
        print("Error: Opción inválida.")
        return

    # Asignar 3 puntos al ganador
    ganador["puntos"] += 3
    equipo_a["partidas_jugadas"] += 1
    equipo_b["partidas_jugadas"] += 1

    # Guardar la partida en el historial
    partida = {
        "equipo1": equipo_a["nombre"],
        "equipo2": equipo_b["nombre"],
        "ganador": ganador["nombre"]
    }
    partidas.append(partida)

    print(f"\n¡'{ganador['nombre']}' ganó la partida y sumó 3 puntos!")


def mostrar_estadisticas():
    """Calcula y muestra el análisis estadístico de los equipos."""

    print("\n--- ESTADÍSTICAS Y RANKING ---")

    if len(equipos) == 0:
        print("No hay equipos registrados aún.")
        return

    # Calcular promedio de puntos usando el módulo statistics
    lista_puntos = []
    for e in equipos:
        lista_puntos.append(e["puntos"])

    promedio = statistics.mean(lista_puntos)

    print(f"\nPromedio de puntos por equipo: {promedio:.2f}")
    print(f"Total de partidas jugadas: {len(partidas)}")

    # Mostrar rendimiento de cada equipo
    print("\n--- RENDIMIENTO POR EQUIPO ---")
    for e in equipos:
        if e["partidas_jugadas"] > 0:
            rendimiento = (e["puntos"] / (e["partidas_jugadas"] * 3)) * 100
        else:
            rendimiento = 0
        print(f"{e['nombre']}: {e['puntos']} pts | Partidas: {e['partidas_jugadas']} | Rendimiento: {rendimiento:.1f}%")

    # Ranking ordenado de mayor a menor puntaje
    print("\n--- RANKING ACTUALIZADO ---")
    ranking = sorted(equipos, key=lambda e: e["puntos"], reverse=True)
    for i, e in enumerate(ranking):
        print(f"{i + 1}. {e['nombre']} - {e['puntos']} puntos")


# ============================================================
# SECCIÓN 4: REPORTES Y CIERRE
# ============================================================

def mostrar_reporte_completo():
    """Muestra un reporte completo del torneo."""

    print("\n" + "=" * 50)
    print("       REPORTE COMPLETO DEL TORNEO")
    print("=" * 50)

    # Lista completa de participantes
    print("\n PARTICIPANTES REGISTRADOS:")
    print("-" * 40)
    if len(participantes) == 0:
        print("No hay participantes registrados.")
    else:
        for i, p in enumerate(participantes):
            estado = "En equipo" if p["en_equipo"] else "Sin equipo"
            print(f"  {i + 1}. {p['nombre']} | Edad: {p['edad']} | Nivel: {p['nivel']} | {estado}")

    # Lista de equipos con integrantes
    print("\n EQUIPOS FORMADOS:")
    print("-" * 40)
    if len(equipos) == 0:
        print("No hay equipos formados.")
    else:
        for e in equipos:
            print(f"  Equipo: {e['nombre']}")
            print(f"    - {e['jugador1']}")
            print(f"    - {e['jugador2']}")
            print(f"    Puntos: {e['puntos']} | Partidas: {e['partidas_jugadas']}")

    # Historial de partidas
    print("\n HISTORIAL DE PARTIDAS:")
    print("-" * 40)
    if len(partidas) == 0:
        print("No se han jugado partidas aún.")
    else:
        for i, p in enumerate(partidas):
            print(f"  Partida {i + 1}: {p['equipo1']} vs {p['equipo2']} → Ganó: {p['ganador']}")

    # Ranking final
    print("\n RANKING FINAL DE EQUIPOS:")
    print("-" * 40)
    if len(equipos) == 0:
        print("No hay equipos para mostrar ranking.")
    else:
        ranking = sorted(equipos, key=lambda e: e["puntos"], reverse=True)
        for i, e in enumerate(ranking):
            print(f"  {i + 1}. {e['nombre']:20} {e['puntos']} puntos")

    print("\n" + "=" * 50)


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    """Muestra el menú principal del sistema."""

    print("\n" + "=" * 50)
    print("   TORNEO DE VIDEOJUEGOS RETRO - PIXELES RETRO")
    print("=" * 50)
    print("1. Registrar participante")
    print("2. Ver participantes")
    print("3. Formar equipo")
    print("4. Ver equipos")
    print("5. Registrar partida")
    print("6. Ver estadísticas y ranking")
    print("7. Reporte completo")
    print("8. Salir")
    print("-" * 50)


def main():
    """Función principal que ejecuta el programa."""

    print("\n¡Bienvenido al Sistema de Gestión del Torneo Pixeles Retro!")

    while True:
        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_participante()
        elif opcion == "2":
            mostrar_participantes()
        elif opcion == "3":
            formar_equipo()
        elif opcion == "4":
            mostrar_equipos()
        elif opcion == "5":
            registrar_partida()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            mostrar_reporte_completo()
        elif opcion == "8":
            print("\n¡Hasta pronto! Gracias por usar el sistema del torneo.")
            break
        else:
            print("Opción inválida. Por favor ingresa un número del 1 al 8.")


# Ejecutar el programa
main()
