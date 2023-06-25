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
    busqueda = input("Ingrese el nombre a buscar")
    notaFinal = 0
    acum=2
    for alumno in archivo.readlines():
        arrayAlumno = alumno.strip().split(";")
        arrayAlumno.pop(-1)
        if arrayAlumno[0]==busqueda:
            arrayAlumno.pop(0)
            arrayAlumno.pop(0)
            for nota in arrayAlumno:
                notaFinal=notaFinal+int(nota)
    notaFinal=notaFinal/6
    print("La nota final de: ",busqueda," es ",notaFinal)
    if notaFinal>7:
        print("Esta aprobado")
    else:
        print("Esta desaprobado")

leeAlumno()