import os
import csv
import matplotlib.pyplot as plt

def main():
   
   #opcion numero 3 del menu principal
    def sub_csv():
       
        
        while True:
            print("\n--- Submenú (.csv) ---")
            print("1. Mostrar las 15 primeras filas")
            print("2. Calcular estadísticas")
            print("3. Graficar una columna completa")
            print("4. Volver al Menú Principal")
            
            opcion = input("Selecciona una opción del submenú (1-4): ")
            archivo= input("ingresa el nombre del archivo .csv:")
            if opcion == '1':
                print("Has elegido mostrar las 15 primeras filas")
                mostrar_15_primeras_filas(archivo)
            elif opcion == '2':
                columna = input("Ingrese el nombre de la columna: ")
                calcular_estadisticas(archivo, columna)
            elif opcion == '3':
            
                print("Has elegido graficar una columna completa")
                columna = input("Ingrese el nombre de la columna: ")
                graficar_columna(archivo, columna)
            elif opcion == '4':
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción no válida en el submenú. Inténtalo de nuevo.")

    def mostrar_15_primeras_filas(archivo):
        try:
            with open(archivo, 'r') as f:
                lector = csv.reader(f)
                for i, fila in enumerate(lector):
                    if i < 15:
                        print(fila)
                    else:
                        break  
        except FileNotFoundError:
            print(f"El archivo '{archivo}' no fue encontrado o no existe.")
       

    def calcular_estadisticas(archivo, columna):
        datos = []
        try:
            with open(archivo, 'r') as file:
                lector = csv.DictReader(file)
                next(lector) 
                for fila in lector:
                    try:
                        dato = float(fila[columna]) 
                        datos.append(dato)
                    except (ValueError, IndexError):
                        continue

            if datos:
                num_datos = len(datos)
                promedio = sum(datos) / num_datos
                datos_ordenados = sorted(datos)
                mediana = datos_ordenados[num_datos // 2] if num_datos % 2 != 0 else \
                  (datos_ordenados[num_datos // 2 - 1] + datos_ordenados[num_datos // 2]) / 2
                maximo = max(datos)
                minimo = min(datos)

                print("Número de datos:", num_datos)
                print("Promedio:", promedio)
                print("Mediana:", mediana)
                print("Máximo:", maximo)
                print("Mínimo:", minimo)
        except FileNotFoundError:
            print("No se encontraron datos en la columna especificada.")


   
    def graficar_columna(archivo, columna): 
        try:
            datos = []
            with open(archivo, 'r') as file:
                lector_csv = csv.DictReader(file)
                for fila in lector_csv:
                    try:
                        datos.append(float(fila[columna]))
                    except ValueError:
                        pass
            if datos:
                plt.plot(datos)
                plt.title(f"Gráfica de la columna {columna}")
                plt.xlabel("Índice")
                plt.ylabel("Valor")
                plt.show()
            else:
                print("No se encontraron datos en la columna especificada.")
        except FileNotFoundError:
            print("el archivo que ingreso no existe.")
    

    def contar_palabras(archivo):
      try:
        contador = 0
        with open(archivo, 'r') as f:
            for linea in f:
                palabras = linea.split()
                contador += len(palabras)
        print(f"El número de palabras es: {contador}")
      except FileNotFoundError:
        print("Error: El archivo no existe o no esta dentro de esta ruta intenta de nuevo")

    def remplazar_palabra(archivo, palabra1, palabra2):
        try:
            with open(archivo, 'r') as f:
                contenido = f.readlines()

                palabras_encontradas = any(palabra1 in linea for linea in contenido)

                while not palabras_encontradas:
                    print(f"La palabra '{palabra1}' no se encontró en el archivo.")
                    palabra1 = input("Introduce una palabra que sí exista en el archivo: ")
                    palabras_encontradas = any(palabra1 in linea for linea in contenido)

                nuevo_contenido = [linea.replace(palabra1, palabra2) for linea in contenido]

            with open(archivo, 'w') as f:
                f.writelines(nuevo_contenido)

            print("Se reemplazó la palabra correctamente.")

        except FileNotFoundError:
            print("el archivo que selecionaste no existen")
    
    def contar_caracteres(archivo):
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
                caracteres = len(contenido)
                caracteres_s_espacio = len(contenido.replace(" ", ""))
                print(f"El archivo tiene {caracteres} caracteres, y sin espacios tiene {caracteres_s_espacio} caracteres.")  
        except FileNotFoundError:
            print("el archivo no existe intente otra vez")

    #opcion numero dos del menu principal
    def sub_txt():
        
        archivo = input("Introduce el nombre del archivo.txt a procesar: ")

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

    #opcion uno del menuprincipal
    def listar_archivos(ruta='.'):
        try:
            archivos = os.listdir(ruta)
            archivos_txt = [archivo for archivo in archivos if archivo.endswith('.txt')]

            if not archivos_txt:
                print("No se encontraron archivos .txt en la ruta especificada.")
            else:
                print(f"Archivos .txt encontrados en la ruta '{ruta}': ")
                for archivo in archivos_txt:
                    print(archivo)
        except FileNotFoundError:
            print(f"'{ruta}'no es una ruta inicie de nuevo")

    #funcion que inicia todo el codigo y nos da el menu
    def menu_principal():  
        while True:
            
            print("\n=== Menú Principal ===")
            print("1. Listar archivos presentes en la ruta actual o ingresar una ruta donde buscar los archivos.")
            print("2. Procesar archivo de texto (.txt)")
            print("3. Procesar archivo separado por comas (.csv)")
            print("4. Salir")

            #¿cual de las 4 opciones escogera el usuario?
            opcion = input("Selecciona una de las opciones (1-4): ")

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
