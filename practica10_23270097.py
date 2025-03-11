import mysql.connector

# Función para establecer la conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="dbtaller"
    )

# Función para crear un nuevo profesor
def crear_profesor():
    nombre = input("Ingresa el nombre del profesor: ").strip()
    apellido = input("Ingresa el apellido del profesor: ").strip()
    especialidad = input("Ingresa la especialidad del profesor: ").strip()
    email = input("Ingresa el email del profesor: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO profesor (nombre, apellido, especialidad, email) VALUES (%s, %s, %s, %s)", 
                       (nombre, apellido, especialidad, email))
        conn.commit()
        print("Profesor creado correctamente.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Función para obtener todos los profesores
def obtener_profesores():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesor")
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    
    print("\nLista de Profesores:")
    for row in resultados:
        print(f"ID: {row[0]} | Nombre: {row[1]} | Apellido: {row[2]} | Especialidad: {row[3]} | Email: {row[4]}")
    print()

# Función para obtener un profesor por su ID
def obtener_profesor():
    profesor_id = input("Ingresa el ID del profesor a buscar: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesor WHERE id = %s", (profesor_id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if resultado:
        print(f"Profesor encontrado: ID: {resultado[0]} | Nombre: {resultado[1]} | Apellido: {resultado[2]} | Especialidad: {resultado[3]} | Email: {resultado[4]}")
    else:
        print("No se encontró el profesor.")

# Función para actualizar un profesor
def actualizar_profesor():
    profesor_id = input("Ingresa el ID del profesor a actualizar: ").strip()
    nuevo_nombre = input("Ingresa el nuevo nombre: ").strip()
    nuevo_apellido = input("Ingresa el nuevo apellido: ").strip()
    nueva_especialidad = input("Ingresa la nueva especialidad: ").strip()
    nuevo_email = input("Ingresa el nuevo email: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE profesor SET nombre = %s, apellido = %s, especialidad = %s, email = %s WHERE id = %s",
                       (nuevo_nombre, nuevo_apellido, nueva_especialidad, nuevo_email, profesor_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Profesor actualizado correctamente.")
        else:
            print("No se encontró el profesor.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Función para eliminar un profesor
def eliminar_profesor():
    profesor_id = input("Ingresa el ID del profesor a eliminar: ").strip()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM profesor WHERE id = %s", (profesor_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Profesor eliminado correctamente.")
        else:
            print("No se encontró el profesor.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Menú principal
def menu():
    while True:
        print("\n MENÚ CRUD - Profesores")
        print("1️. Crear profesor")
        print("2️. Ver todos los profesores")
        print("3️. Buscar un profesor")
        print("4️. Actualizar un profesor")
        print("5️. Eliminar un profesor")
        print("0️. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            crear_profesor()
        elif opcion == "2":
            obtener_profesores()
        elif opcion == "3":
            obtener_profesor()
        elif opcion == "4":
            actualizar_profesor()
        elif opcion == "5":
            eliminar_profesor()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
