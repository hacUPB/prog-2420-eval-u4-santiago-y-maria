import os

def main():
    def sub_csv():
        while True:
            print("\n--- Submenú (.csv) ---")
            print("1. Mostrar las 15 primeras filas")
            print("2. Calcular estadísticas")
            print("3. Graficar una columna completa")
            print("4. Volver al Menú Principal")
            
            opcion = input("Selecciona una opción del submenú (1-4): ")
            
            if opcion == '1':
                print("Has elegido mostrar las 15 primeras filas")
                
            elif opcion == '2':
                print("Has elegido calcular estadísticas")
                
            elif opcion == '3':
                print("Has elegido graficar una columna completa")
                
            elif opcion == '4':
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción no válida en el submenú. Inténtalo de nuevo.")

    def sub_txt():
        archivo = input("Introduce el nombre del archivo .txt a procesar: ")

        while True:
            print("\n--- Submenú (.txt) ---")
            print("1. Contar el número de palabras")
            print("2. Reemplazar una palabra por otra")
            print("3. Contar caracteres")
            print("4. Volver al Menú Principal")
            
            opcion = input("Selecciona una opción del submenú (1-4): ")
        
            if opcion == '1':
                print("Has elegido contar el número de palabras")
                contar_palabras(archivo)           
            elif opcion == '2':
                print("Has elegido reemplazar una palabra por otra")
                palabra1 = input("Introduce la palabra a reemplazar: ")
                palabra2 = input("Introduce la nueva palabra: ")
                remplazar_palabra(archivo, palabra1, palabra2)  
            elif opcion == '3':
                print("Has elegido contar el número de caracteres")
                contar_caracteres(archivo)
            elif opcion == '4':
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción no válida en el submenú. Inténtalo de nuevo.")

    def contar_palabras(archivo):
        contador = 0
        with open(archivo, 'r') as f:
            for linea in f:
                palabras = linea.split()
                contador += len(palabras)
        print(f"El número de palabras es: {contador}")
        return contador

    def remplazar_palabra(archivo, palabra1, palabra2):
        with open(archivo, 'r') as f:
            contenido = f.readlines()

        nuevo_contenido = [linea.replace(palabra1, palabra2) for linea in contenido]

        with open(archivo, 'w') as f:
            f.writelines(nuevo_contenido)

        print("Se reemplazó la palabra correctamente.")

    def contar_caracteres(archivo):
        with open(archivo, 'r') as f:
            contenido = f.read()
            caracteres = len(contenido)
            caracteres_s_espacio = len(contenido.replace(" ", ""))
        print(f"El archivo tiene {caracteres} caracteres, y sin espacios tiene {caracteres_s_espacio} caracteres.")

    def listar_archivos(ruta='.'):
        archivos = os.listdir(ruta)
        archivos_txt = [archivo for archivo in archivos if archivo.endswith('.txt')]

        if not archivos_txt:
            print("No se encontraron archivos .txt en la ruta especificada.")
        else:
            print("Archivos .txt encontrados:")
            for archivo in archivos_txt:
                print(archivo)

    def menu_principal():
        while True:
            print("\n=== Menú Principal ===")
            print("1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos.")
            print("2. Procesar archivo de texto (.txt)")
            print("3. Procesar archivo separado por comas (.csv)")
            print("4. Salir")

            opcion = input("Selecciona una opción (1-4): ")

            if opcion == '1':
                print("Opción 1 elegida")
                ruta = input("Introduce la ruta (deja vacío para usar la ruta actual): ")
                listar_archivos(ruta if ruta else '.')
            elif opcion == '2':
                print("Has elegido ir al submenú (.txt)")
                sub_txt()
            elif opcion == '3':
                print("Has elegido ir al submenú (.csv)")
                sub_csv()
            elif opcion == '4':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida en el menú. Inténtalo de nuevo.")

    menu_principal()

if __name__ == "__main__":
    main()
