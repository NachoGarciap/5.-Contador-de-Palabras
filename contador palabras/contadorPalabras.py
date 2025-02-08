import os


class ContadorPalabras:

    def __init__(self):
        print('----- Contador de Palabras -----')

    def crear_archivo(self):
        try:
            nombre_archivo = input('Introduce el nombre del archivo: ')
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                print(f'Archivo "{nombre_archivo}" creado correctamente.')
        except Exception as e:
            print(f'Error al crear el archivo: {e}')

    def listar_archivos(self):
        print('\n ----- Archivos en el directorio actual -----')
        archivos = [f for f in os.listdir() if os.path.isfile(f)]  # Solo archivos, no carpetas
        if archivos:
            for archivo in archivos:
                print(f'{archivo}')
        else:
            print('⚠️ No hay archivos en el directorio.')

    def escribir_archivo(self):
        nombre_archivo = input('Introduce el nombre del archivo donde quieres escribir: ')

        if not os.path.exists(nombre_archivo):
            print('El archivo no existe. Primero debes crearlo.')
            return

        try:
            with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
                texto = input('Escribe el texto que quieres guardar en el archivo:\n')
                archivo.write(texto + '\n')  # Agrega texto con un salto de línea
                print('Texto guardado correctamente.')
        except Exception as e:
            print(f'Error al escribir en el archivo: {e}')

    def leer_archivo(self):
        try:
            nombre_archivo = input('Introduce el nombre del archivo que quieres leer: ')
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                if contenido.strip():  # Verifica si el archivo tiene contenido
                    print('\n----- Contenido del Archivo -----')
                    print(contenido)
                else:
                    print('El archivo está vacío.')
        except FileNotFoundError:
            print('Error: El archivo no existe. Verifica el nombre e intenta de nuevo.')
        except Exception as e:
            print(f'Error al leer el archivo: {e}')

    def contar_palabras_caracteres(self):
        nombre_archivo = input('Introduce el nombre del archivo que quieres analizar: ')

        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                texto = archivo.read().strip() # Ahora cuenta correctamente sin el salto de linea
                palabras = texto.split()
                num_palabras = len(palabras)
                num_caracteres = len(texto)
                print(f'📊 Número de palabras: {num_palabras}')
                print(f'📊 Número de caracteres: {num_caracteres}')
        except FileNotFoundError:
            print('Error: El archivo no existe.')
        except Exception as e:
            print(f'Error al leer el archivo: {e}')

    def menu(self):
        while True:
            print('\n----- Menú -----')
            print('1. Crear un nuevo archivo')
            print('2. Listar archivos')
            print('3. Escribir en el archivo')
            print('4. Leer texto')
            print('5. Contar palabras y caracteres')
            print('6. Salir')

            opcion = input('Elige una opción: ')

            if opcion == '1':
                self.crear_archivo()
            elif opcion == '2':
                self.listar_archivos()
            elif opcion == '3':
                self.escribir_archivo()
            elif opcion == '4':
                self.leer_archivo()
            elif opcion == '5':
                self.contar_palabras_caracteres()
            elif opcion == '6':
                print('Saliendo del programa...')
                break
            else:
                print('Opción no válida, intenta de nuevo.')