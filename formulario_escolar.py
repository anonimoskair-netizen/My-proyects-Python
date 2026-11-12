import time

data = {
    "students": [],
    "encargados": []
}

def DataStudent():
    grado = input("\nIngresa el grado que cursas: ")
    seccion = input("¿A qué sección perteneces?: ")
    nie = input("Ingresa tu NIE: ")
    sexo = input("Selecciona tu sexo F/M: ")
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    tel = input("Ingresa tu número de teléfono: ")
    nombre_encargado = input("Ingresa el nombre de tu encargado/a: ")

    return {
        "gr": grado, 
        "sec": seccion, 
        "nie": nie, 
        "sex": sexo, 
        "nom": nombre, 
        "edad": edad, 
        "tel": tel, 
        "n_e": nombre_encargado
    }

def DataEncargado():
    nombre_responsable = input("\nIngresa tu nombre: ")
    edad_responsable = input("Ingresa tu edad: ")
    telefono = input("Ingresa tu número de teléfono: ")
    nombre_estudiante = input("Ingresa el nombre del estudiante a cargo: ")

    return {
        "n": nombre_responsable, 
        "e": edad_responsable, 
        "t": telefono, 
        "n_e": nombre_estudiante
    }

def RegistrosEstudiantes():
    if not data["students"]:
        print("\nNo hay estudiantes registrados.")
    else:
        print("\n--- LISTA DE ESTUDIANTES ---")
        for i in data["students"]:
            print(f"\nGrado: {i['gr']} | Sección: {i['sec']} | NIE: {i['nie']} | Sexo: {i['sex']} | Nombre: {i['nom']} | Edad: {i['edad']} | Teléfono: {i['tel']} | Encargado: {i['n_e']}")

def RegistrosEncargados():
    if not data["encargados"]:
        print("\nNo hay encargados registrados.")
    else:
        print("\n--- LISTA DE ENCARGADOS ---")
        for i in data["encargados"]:
            print(f"\nNombre: {i['n']} | Edad: {i['e']} | Teléfono: {i['t']} | Estudiante a cargo: {i['n_e']}")

def GuardarDatosEstudiante():
    nuevo_estudiante = DataStudent()
    data["students"].append(nuevo_estudiante)
    print("\n¡Estudiante registrado con éxito!")

def GuardarDatosEncargado():
    nuevo_encargado = DataEncargado()
    data["encargados"].append(nuevo_encargado)
    print("\n¡Encargado registrado con éxito!")

def Salir():
    print("\nSaliendo...")
    time.sleep(3)
    exit()

menu = {
    1: GuardarDatosEstudiante,
    2: GuardarDatosEncargado,
    3: RegistrosEstudiantes,
    4: RegistrosEncargados,
    5: Salir
}

while True:
    print("\n----Menú----")
    print("1. Ingresar datos de estudiante")
    print("2. Ingresar datos del encargado/a")
    print("3. Ver estudiantes registrados")
    print("4. Ver encargados registrados")
    print("5. Salir")

    opcion = input("\nIngresa tu opción: ")

    try:
        user_opcion = int(opcion)
        if user_opcion < 1 or user_opcion > 5:
            print("\nOpción no valida")
            continue
    except ValueError:
        print("\nSolo números")
        continue

    if user_opcion in menu:
        accion = menu[user_opcion]
        accion()
