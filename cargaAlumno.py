
def agregaAlumno():
    archivo = open("alumnos.txt", "w")
    cargaAlumno="si"

    while cargaAlumno != "no":
        nombre = input("Ingrese nombre y apellido: ")
        acum = 0
        dni = int(input("Ingrese el DNI del alumno"))
        archivo.write(nombre)
        archivo.write(";")
        archivo.write(str(dni))
        archivo.write(";")
        while acum<6:
            nota = int(input("Ingrese una nota"))
            if nota>10 or nota<1:
                print("Ingrese una nota del 1 al 10: ")
                continue
            else:
                acum = acum+1
                archivo.write(str(nota))
                archivo.write(";")
                print("Usted puso de nota ", nota," al tp ",acum)
        cargaAlumno= input("Si no quiere cargar mas alumnos ingrese (No)")
        cargaAlumno= cargaAlumno.lower()
        archivo.write("\n")
    archivo.close()

def leeAlumno():
    archivo = open("alumnos.txt", "r")
    busqueda = input("Ingrese el nombre a buscar: ")
    notaFinal = 0
    for alumno in archivo.readlines():
        arrayAlumno = alumno.strip().split(";")
        arrayAlumno.pop(-1)
        if arrayAlumno[0]==busqueda:
            arrayAlumno.pop(0)
            arrayAlumno.pop(0)
            for nota in arrayAlumno:
                notaFinal=notaFinal+int(nota)

    if notaFinal>0:
        notaFinal=notaFinal/6
        print("La nota final de: ",busqueda," es ",notaFinal)
        if notaFinal>=7:
            print("Esta aprobado")
        else:
            print("Esta desaprobado")
    else:
        print("Ese usuario no existe")

    archivo.close()

def estadoEstudiantes():
    archivo = open("alumnos.txt", "r")
    aprobado = []
    desaprobado=[]
    nota=0
    for alumno in archivo.readlines():
        alumno=alumno.strip().split(";")
        nombre = alumno[0]
        alumno.pop(-1)
        alumno.pop(0)
        alumno.pop(0)
        for notas in alumno:
            notas = int(notas)
            nota=notas+nota
        nota=nota/6
        if nota>=7:
            aprobado.append(nombre)
            continue
        else:
            desaprobado.append(nombre)
            continue
    opcion = int(input("Si quiere buscar aprobados ingrese 1, para los desaprobados ingrese 2: "))
    if opcion==1:
        print("Los aprobados son: ")
        for alumno in aprobado:
            print(alumno)
    elif opcion == 2:
        print("Los desaprobados son: ")
        for alumno in desaprobado:
            print(alumno)
    archivo.close()


def menu():
    opcion=input("Para agregar alumno ingrese 1\nPara buscar un alumno ingrese 2\n Para ver aprobados ingrese 3\n Para salir presione enter: ")
    while opcion== "1" or "2" or "3":
        if opcion=="1":
            agregaAlumno()
            opcion=input("Para agregar alumno ingrese 1\nPara buscar un alumno ingrese 2\n Para ver aprobados ingrese 3\n Para salir presione enter: ")
        elif opcion =="2":
            leeAlumno()
            opcion=input("Para agregar alumno ingrese 1\nPara buscar un alumno ingrese 2\n Para ver aprobados ingrese 3\n Para salir presione enter: ")

        elif opcion == "3":
            estadoEstudiantes()
            opcion=input("Para agregar alumno ingrese 1\nPara buscar un alumno ingrese 2\n Para ver aprobados ingrese 3\n Para salir presione enter: ")
        else:
            break

menu()
print("Usted salio")