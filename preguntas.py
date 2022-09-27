"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
with open("data.csv", "r") as file:
        datos = file.readlines()

datos = [row.rstrip("\n").split() for row in datos]

def pregunta_01():
    
    suma = sum([int(datos[i][1]) for i in range(len(datos))])
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return suma


def pregunta_02():

    letrastotal = [row[0] for row in datos]
    letras = set(row[0] for row in datos)
    repeticiones = sorted([(letra,letrastotal.count(letra)) for letra in letras], key = lambda x:x[0])
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    return repeticiones


def pregunta_03():

    suma=dict()

    for row in datos:
        try:
            suma[row[0]]+=int(row[1])
        except KeyError:
            suma[row[0]]=int(row[1])

    respuesta=sorted([(key,value) for key,value in suma.items()], key = lambda x:x[0])


    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return respuesta


def pregunta_04():

    meses=[row[2].split("-")[1] for row in datos]
    reps={mes:meses.count(mes) for mes in meses}
    respuesta=sorted([(key,value) for key,value in reps.items()], key = lambda x:x[0])
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return respuesta


def pregunta_05():

    letras = set(row[0] for row in datos)
    respuesta=[]

    for i in letras:
        minimo=10000
        maximo=0
        for row in datos:
            if row[0]==i:
                if int(row[1])>maximo:
                    maximo=int(row[1])
                if int(row[1])<minimo:
                    minimo=int(row[1])
        respuesta.append((i,maximo,minimo))

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return sorted(respuesta, key=lambda x:x[0])


def pregunta_06():

    info = [elemento.split(":") for row in datos for elemento in row[4].split(",")]
    unicos = {i[0] for i in info}
    respuesta = []
    for i in unicos:
            minimo=10000
            maximo=0
            for par in info:
                if par[0] == i:
                    if int(par[1]) > maximo:
                        maximo = int(par[1])
                    if int(par[1]) < minimo:
                        minimo = int(par[1])
            respuesta.append((i,minimo,maximo))

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return sorted(respuesta, key=lambda x:x[0])


def pregunta_07():

    dicc={}
    for row in datos:
        if int(row[1]) not in dicc.keys():
            dicc[int(row[1])] = [row[0]]
        else:
            dicc[int(row[1])].append(row[0])
    respuesta = sorted([(key,value) for key,value in dicc.items()], key = lambda x:x[0])

    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return respuesta


def pregunta_08():

    dicc={}
    for row in datos:
        if int(row[1]) not in dicc.keys():
            dicc[int(row[1])] = [row[0]]
        else:
            dicc[int(row[1])].append(row[0])

    respuesta = sorted([(key,sorted(list(set(value)))) for key,value in dicc.items()], key = lambda x:x[0])

    """ OTRA FORMA DE HACERLO
    for row in datos:
        if int(row[1]) not in dicc.keys():
            dicc[int(row[1])] = [row[0]]
        elif row[0] not in dicc[int(row[1])]:
            dicc[int(row[1])].append(row[0])

    respuesta = sorted([(key,sorted(value)) for key,value in dicc.items()], key = lambda x:x[0]) """

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return respuesta


def pregunta_09():

    info = [elemento.split(":")[0] for row in datos for elemento in row[4].split(",")]
    repeticiones = {i:info.count(i) for i in sorted(set(info))}

    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return repeticiones


def pregunta_10():

    respuesta = [(row[0],len(row[3].split(",")),len(row[4].split(","))) for row in datos]

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return respuesta


def pregunta_11():

    dicc={}
    for row in datos:
        for letra in row[3].split(","):
            if letra not in dicc.keys():
                dicc[letra] = int(row[1])
            else:
                dicc[letra] += int(row[1])

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return  dict(sorted(dicc.items(), key=lambda x:x[0]))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
