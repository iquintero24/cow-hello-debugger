"""
🐄 COW DEBUGGER 🧠

Este script es una guía paso a paso para crear tu propio debugger (depurador)
para el lenguaje esotérico Cow, escrito en Python. Te permite ejecutar código
Cow paso a paso, viendo cómo cambian la memoria, el puntero, el portapapeles,
y la salida mientras se interpreta.

Ideal para aprender cómo funciona Cow, practicar programación y enseñar a otros.
Puedes usar este archivo como un TODO para marcar tu progreso mientras lo implementas.
"""

# ✅ 1. Cargar el código Cow desde un archivo o string
# TODO: Abrir el archivo hello_world.cow y guardar el código
# TODO: Separar el código por espacios y filtrar solo comandos válidos

# ✅ 2. Inicializar las estructuras básicas
# TODO: Crear lista de instrucciones válidas (MoO, Moo, etc)
# TODO: Inicializar memoria con 100 celdas (puedes usar [0]*100)
# TODO: Inicializar el puntero (pointer = 0)
# TODO: Inicializar output (texto que se imprimirá)
# TODO: Inicializar clipboard para MMM

# ✅ 3. Ejecutar paso a paso con while loop
# TODO: Crear un while que recorra las instrucciones (ip < len(instructions))
# TODO: Leer la instrucción actual y procesarla con if/elif

# ✅ 4. Implementar comandos Cow básicos
# TODO: "MoO" - sumar 1 a la celda actual
# TODO: "MOo" - restar 1
# TODO: "moO" - mover el puntero a la derecha
# TODO: "mOo" - mover el puntero a la izquierda
# TODO: "Moo" - si valor > 0 imprimirlo como ASCII, si es 0 pedir input
# TODO: "MMM" - si clipboard vacío, copiar valor actual. Si no, pegar
# TODO: "OOM" - mostrar número como salida (opcional)

# ✅ 5. Mostrar estado para debug paso a paso
# TODO: Imprimir número de paso y comando actual
# TODO: Mostrar puntero, memoria (primeros 10 slots), output, clipboard
# TODO: Pausar con input() para avanzar paso a paso

# ✅ 6. Extensiones futuras (cuando termines lo básico)
# TODO: Soporte para bucles (MOO ... moo)
# TODO: Soporte para mOO (ejecutar contenido como código Cow)
# TODO: Interfaz visual (Tkinter / curses)

# 🎯 BONUS: Guardar un historial de estados (para retroceder pasos)
# TODO: Guardar memoria/puntero/output en cada paso en una lista

# ¡Comienza tu implementación debajo de esta línea 👇!

# ... tu código aquí ...
