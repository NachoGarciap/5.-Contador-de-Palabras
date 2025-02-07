import os


class ContadorPalabras:

    def __init__(self):
        print('----- Contador de Palabras -----')
        self.nombre_archivo = None  # Para almacenar el nombre del archivo

    def crear_archivo(self):
        try:
            self.nombre_archivo = input('Introduce el nombre del archivo: ')
            with open(self.nombre_archivo, 'w', encoding='utf-8') as archivo:
                print(f'Archivo "{self.nombre_archivo}" creado correctamente.')
        except Exception as e:
            print(f'Error al crear el archivo: {e}')

    def listar_archivos(self):
        print('\n----- Archivos en el directorio actual -----')
        archivos = [f for f in os.listdir()]
        if archivos:
            for archivo in archivos:
                print(f'- {archivo}')
        else:
            print('No hay archivos en el directorio.')

    def escribir_archivo(self):
        if not self.nombre_archivo:
            print('Primero debes crear un archivo.')
            return

        try:
            with open(self.nombre_archivo, 'a', encoding='utf-8') as archivo:
                texto = input('Escribe el texto que quieres guardar en el archivo:\n')
                archivo.write(texto + '\n')  # Se agrega el texto con un salto de línea
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
        if not self.nombre_archivo:
            print('Primero debes crear un archivo.')
            return

        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                texto = archivo.read().strip()  # Elimina espacios y saltos de línea extra
                palabras = texto.split()
                num_palabras = len(palabras)
                num_caracteres = len(texto)  # Ahora cuenta correctamente sin el \n extra
                print(f'Número de palabras: {num_palabras}')
                print(f'Número de caracteres: {num_caracteres}')
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