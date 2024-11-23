import os

def obtener_comparaciones_archivos(lista_archivos: list, n: int, directorio: str) -> tuple[list, list]:
    '''
    Obtiene las comparaciones de similitud entre los archivos de una lista.

    Precondiciones:
    - 'lista_archivos' es una lista de rutas de archivos de texto en el directorio dado.
    - 'n' es un entero que es el tamaño de los n-gramas.
    - 'directorio' es una cadena que representa la ruta del directorio donde se encuentran los archivos.

    Postcondiciones:
    - Devuelve una tupla con dos listas de tuplas, la primera contiene los resultados sospechosos y la segunda los resultados generales.
    '''
    resultados_sospechos = []
    resultados_generales = []
    for i in range(len(lista_archivos)):
        for j in range(i + 1, len(lista_archivos)):
            ngramas_i = obtener_cantidad_ngramas(lista_archivos[i], n)  # 1er archivo
            ngramas_j = obtener_cantidad_ngramas(lista_archivos[j], n)  # 2do archivo

            similitud = calcular_coeficiente_jaccard(ngramas_i, ngramas_j)

            archivo1 = lista_archivos[i][len(directorio)+1:]
            archivo2 = lista_archivos[j][len(directorio)+1:]

            if similitud >= 0.01:
                resultados_generales.append((archivo1, archivo2, similitud))

            if similitud >= 0.15:
                resultados_sospechos.append((archivo1, archivo2, similitud))

    return resultados_sospechos, resultados_generales


def obtener_archivos_directorio(directorio: str) -> list:
    '''
    Obtiene los archivos de un directorio dado.

    Parametros:
        directorio (str): Ruta del directorio del cual se desean obtener los archivos.

    Devuelve:
        lista: Lista de rutas de los archivos encontrados en el directorio (con os).
    '''
    archivos = []

    for file in os.listdir(directorio):
        if file.endswith('.txt'):
            archivos.append(os.path.join(directorio, file))

    return archivos


def obtener_lista_limpia(linea: str) -> list[str]:
    '''
    Limpia una linea de texto, conservando solo caracteres alfanumericos a minusculas y espacios, 
    Devuelve una lista de palabras.

    Precondiciones:
    - 'linea' es una cadena de texto.
    
    Postcondiciones:
    - Devuelve una lista de palabras minusculas y con espacios.
    - La lista puede estar vacia si 'linea' no contiene caracteres alfabeticos.
    '''

    caracteres = []
    for caracter in linea:
        if caracter.isalpha() or caracter == ' ':
            caracteres.append(caracter.lower())
    linea_limpia = ''.join(caracteres)
    return linea_limpia.split() # type: ignore


def obtener_cantidad_ngramas(ruta_archivo: str, n: int) -> dict:
    '''
    Precondiciones: 
    - 'ruta_archivo' es una cadena de texto que representa la ruta de un archivo de texto.
    Postcondiciones:
    - Devuelve un diccionario donde las claves son tuplas de palabras (n-gramas) y los valores son la frecuencia de cada n-grama
    '''
    dicc_gramas: dict[tuple, int] = {}
    lista_palabras_aux = []

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                palabras = obtener_lista_limpia(linea)
                # Crea n-gramas palabra a palabra
                for palabra in palabras:
                    # Si lista de palabras aux esta llena:
                    if len(lista_palabras_aux) == n:
                        n_grama = tuple(lista_palabras_aux)

                        if n_grama not in dicc_gramas:
                            dicc_gramas[n_grama] = 0

                        dicc_gramas[n_grama] += 1
                        lista_palabras_aux.pop(0)

                    lista_palabras_aux.append(palabra)

        return dicc_gramas
    except FileNotFoundError:
        print("Ha ocurrido un error al buscar el archivo")
    except IOError:
        print("Ha ocurrido un error al leer el archivo")


def calcular_coeficiente_jaccard(gramas1: dict[tuple, int], gramas2: dict[tuple, int]) -> float:
    '''
    Precondiciones:
    - 'gramas1' y 'gramas2' son diccionarios donde las claves son tuplas de palabras (n-gramas).
    Postcondiciones:
    - Devuelve un flotante para el coeficiente de jaccard.
    - El valor está entre [0, 1]
    '''
    suma_interseccion = 0
    suma_union = 0

    for clave1, valor1 in gramas1.items():
        if clave1 in gramas2:
            suma_interseccion += valor1 + gramas2[clave1]
        suma_union += valor1

    suma_union += sum(gramas2.values())

    return suma_interseccion / suma_union if suma_union != 0 else 0
