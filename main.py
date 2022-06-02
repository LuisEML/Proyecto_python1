"""Proyecto python + MySQL:
1. Abrir el asiste
2. Loginyregistro
3. Si elegimos registro,creara un usuario en la BD
4. Si elegimos login,identificara al usuarioynos preguntara
5. Crear nota,mostrar notas, o borrarlas
"""



from usuarios import acciones

print("""
Acciones disponibles:
    1-registro
    2-login
""")


hazEl = acciones.Acciones()

accion = input("Que quieres hacer?")

if accion == "1":
    hazEl.registro()



elif accion == "2":
    hazEl.login()



print("\n")
print("Nombre:Luis Enrique Mendez Lezama")
print("Grupo: 9° A")
print("Materia: Desarrollo para dispositivos inteligentes")
print("Fecha: 1/06/2022")