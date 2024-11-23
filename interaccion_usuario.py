"""intereaccion usuario module"""
import os

def pedir_directorio() -> str:
    '''
    Pide al usuario ingresar un directorio y verifica su validez.

    Precondiciones:
    - El usuario debe ingresar inputs

    Postcondiciones:
    - Devuelve una cadena que representa una ruta de directorio valida o una cadena vacia si el usuario decide salir.
    '''
    directorio = input('Ingrese un directorio (deje vacio para salir): ')
    if not directorio:
        return directorio
    while not os.path.isdir(directorio):
        print('Directorio invalido.')
        directorio = input('Ingrese un directorio: ')
        if not directorio:
            return directorio
    return directorio


def pedir_N_gramas() -> int:
    ''' 
    Pide al usuario ingresar un número N para los n-gramas y verifica su validez.

    Precondiciones:
    - El usuario debe ingresar un numero entero entre 2 y 10.

    Postcondiciones:
    - Devuelve un entero que es la cantidad N de n-gramas ingresado por el usuario.
    '''
    N = input('Ingrese un numero N de n-gramas: ')
    while not N.isdigit() or int(N) < 2 or int(N) > 10:
        print('Numero invalido.')
        N = input('Ingrese un numero N de n-gramas: ')
    return int(N)


def mostrar_resultados_sospechosos(resultados_sospechosos: list) -> None:
    '''
    Muestra en pantalla los resultados sospechosos de las comparaciones.

    Precondiciones:
    - 'resultados_sospechosos' es una lista de tuplas que contienen los nombres de los archivos y su similitud.

    Postcondiciones:
    - Muestra en pantalla los resultados sospechosos de las comparaciones.
    '''
    print("\nResultados sospechosos: ")
    resultados_sospechosos.sort(key=lambda x: x[2], reverse=True)
    for archivo1, archivo2, similitud in resultados_sospechosos:
        print(f'- {archivo1} y {archivo2}: {similitud*100:.2f}%')

def pedir_nombre_reporte() -> str:
    '''
    Pide al usuario ingresar un nombre para el archivo de reporte.

    Precondiciones:
    - El usuario debe ingresar un texto que represente el nombre del archivo.

    Postcondiciones:
    - Devuelve una cadena que representa el nombre del archivo, se asegura que termine en ".csv".
    '''
    nombre_reporte = input('\nIngrese un nombre para el archivo de reporte: ')
    if not nombre_reporte:
        return ''
    if nombre_reporte.endswith('.csv'):
        return nombre_reporte
    return nombre_reporte + '.csv'


def crear_archivo_reporte(ruta_nueva: str, resultados_generales: list[tuple]) -> None:
    '''
    Crea un archivo con los resultados generales de las comparaciones.
    
    Precondiciones:
    - 'ruta_nueva' es una cadena que representa la ruta del archivo.
    - 'resultados_generales' es una lista de tuplas que contienen los nombres de los archivos y su similitud.

    Postcondiciones:
    - Crea un archivo con los resultados generales de las comparaciones.
    '''
    if not ruta_nueva:
        return
    try:
        with open(ruta_nueva, 'w') as archivo:
            archivo.write('Archivo1,Archivo2,Similitud\n')
            resultados_generales.sort(key=lambda x: x[2], reverse=True)
            for archivo1, archivo2, similitud in resultados_generales:
                archivo.write(f'{archivo1},{archivo2},{similitud*100:.2f}%\n')
    except PermissionError:
        print(f"Permiso denegado: '{ruta_nueva}'. Revisa tus permisos.")
    except IOError as e:
        print(f"Un Erro de IO ocurrido: {e.strerror}")
