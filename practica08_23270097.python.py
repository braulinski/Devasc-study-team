import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="investigacion"
)

cursor = conexion.cursor()

def crear_linea(nombre, descripcion):
    cursor.execute("INSERT INTO lineas_investigacion (nombre, descripcion) VALUES (%s, %s)", (nombre, descripcion))
    conexion.commit()
    print("Línea de investigación creada exitosamente.")

def leer_lineas():
    cursor.execute("SELECT * FROM lineas_investigacion")
    lineas = cursor.fetchall()
    for linea in lineas:
        print(linea)

def actualizar_linea(id_linea, nuevo_nombre, nueva_descripcion):
    cursor.execute("UPDATE lineas_investigacion SET nombre = %s, descripcion = %s WHERE id = %s", 
                   (nuevo_nombre, nueva_descripcion, id_linea))
    conexion.commit()
    print("Línea de investigación actualizada.")

def eliminar_linea(id_linea):
    cursor.execute("DELETE FROM lineas_investigacion WHERE id = %s", (id_linea,))
    conexion.commit()
    print("Línea de investigación eliminada.")

while True:
    print("\n--- CRUD de Líneas de Investigación ---")
    print("1. Crear línea de investigación")
    print("2. Leer líneas de investigación")
    print("3. Actualizar línea de investigación")
    print("4. Eliminar línea de investigación")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la línea de investigación: ")
        descripcion = input("Descripción: ")
        crear_linea(nombre, descripcion)

    elif opcion == "2":
        print("\nLíneas de investigación registradas:")
        leer_lineas()

    elif opcion == "3":
        id_linea = int(input("ID de la línea a actualizar: "))
        nuevo_nombre = input("Nuevo nombre: ")
        nueva_descripcion = input("Nueva descripción: ")
        actualizar_linea(id_linea, nuevo_nombre, nueva_descripcion)

    elif opcion == "4":
        id_linea = int(input("ID de la línea a eliminar: "))
        eliminar_linea(id_linea)

    elif opcion == "5":
        conexion.close()
        break

    else:
        print("Opción no válida. Intenta de nuevo.")