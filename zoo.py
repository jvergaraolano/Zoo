def zoologico(n):
    """
    Procedimiento que analiza el comportamiento de las entradas al zoológico.
    Entradas: n es un entero positivo que representa el número de encuestados
    Salida: Impresión por pantalla de los datos
    """
    menores = 0
    mayores = 0
    contador = 1
    masPersona = ""
    memPersona = 0
    cantMayores = 0
    cantMenores = 0
    felinos = 0
    acuario = 0
    aves = 0
    serpientes = 0
    while (contador <= n):
        # Preguntas a los usuarios
        nombre = (input("Nombre?"))
        edad = eval(input("Edad?"))
        veces = eval(input("Cuántas veces va al zoológico al año?"))
        area = (input("Área preferida del zoo (felinos/acuario/aves/serpiente)"))

        # Determina quienes son mayores o menores de edad
        if (edad >= 18):
            mayores = mayores + 1
            cantMayores = cantMayores + veces
        elif (edad < 18):
            menores = menores + 1
            cantMenores = cantMenores + veces

        if (area == "felinos"):
            felinos = felinos + 1
        elif (area == "acuario"):
            acuario = acuario + 1
        elif (area == "aves"):
            aves = aves + 1
        elif (area == "serpientes"):
            serpientes = serpientes + 1

        if (veces > memPersona):
            masPersona = nombre
            memPersona = veces

        contador = contador + 1

    if (felinos > acuario and felinos > aves and felinos > serpientes):
        area = "Felinos"
    elif (acuario > felinos and acuario > aves and acuario > serpientes):
        area = "Acuario"
    elif (aves > acuario and aves > felinos and aves > serpientes):
        area = "Aves"
    elif (serpientes > aves and serpientes > felinos and serpientes > acuario):
        area = "Serpientes"

    promMayores = cantMayores / mayores
    promMenores = cantMenores / menores
    print("Cantidad de visitantes mayores de edad: " + str(mayores))
    print("Cantidad de visitantes menores de edad: " + str(menores))
    print("Promedio de visita de mayores de edad: " + str(promMayores))
    print("Promedio de visita de menores de edad: " + str(promMenores))
    print("Área más visitada del zoológico: " + area)
    print("Persona que más visita el zoológico: " + masPersona)