"""main module"""
from procesamiento import obtener_archivos_directorio, obtener_comparaciones_archivos
from interaccion_usuario import (
    crear_archivo_reporte,
    pedir_directorio,
    pedir_N_gramas,
    pedir_nombre_reporte,
    mostrar_resultados_sospechosos,
)


def main() -> None:
    '''
    Función principal del programa que maneja el flujo de interacción con el usuario.
    
    Precondiciones:
    - Ninguna.
    
    Postcondiciones:
    - El programa solicita al usuario un directorio, un número N para n-gramas, y un nombre para el archivo de reporte.
    - Se realizan comparaciones de archivos en el directorio y se guarda un reporte con los resultados.
    '''
    while True:
        directorio = pedir_directorio()
        if not directorio:
            return

        N = pedir_N_gramas()
        lista_archivos = obtener_archivos_directorio(directorio)

        resultados_sospechosos, resultados_generales = obtener_comparaciones_archivos(lista_archivos, N, directorio)

        mostrar_resultados_sospechosos(resultados_sospechosos)

        nombre_reporte = pedir_nombre_reporte()
        crear_archivo_reporte(nombre_reporte, resultados_generales)

if __name__ == '__main__':
    main()
