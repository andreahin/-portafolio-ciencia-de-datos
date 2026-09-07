# Sistema de Gestión de Torneo de Videojuegos Retro

**Módulo:** Fundamentos de Python (estructuras de datos, funciones y validaciones)

## Descripción

Programa en Python que simula la gestión completa de un torneo de videojuegos retro para el arcade ficticio "Pixeles Retro": registro de participantes, formación de equipos, registro de partidas y generación de reportes estadísticos.

## Funcionalidades

- **Registro de participantes** con validación de nombre, edad (12-70 años) y nivel de experiencia (1-5).
- **Formación de equipos** de 2 jugadores, verificando que ningún jugador quede en más de un equipo y que el nombre del equipo sea único.
- **Registro de partidas** entre equipos, con asignación automática de 3 puntos al equipo ganador.
- **Análisis estadístico** con el módulo `statistics`: promedio de puntos por equipo, rendimiento porcentual y ranking actualizado.
- **Reporte completo** del torneo: participantes, equipos, historial de partidas y ranking final, con formato ordenado y legible.

## Tecnologías

- Python 3
- Módulo `statistics` de la librería estándar
- Estructuras de datos: listas y diccionarios
- Funciones con parámetros y valores de retorno

## Cómo ejecutarlo

```bash
python torneo_videojuegos.py
```

El programa despliega un menú interactivo por consola con 8 opciones (registrar participante, ver participantes, formar equipo, ver equipos, registrar partida, ver estadísticas, reporte completo, salir).
