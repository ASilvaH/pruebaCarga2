# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # función para imprimir los datos

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    # función para obtener el resultado

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")


# bloque principal creamos los nuevos objetos pasándoles los parámetros nombre y nota tal como indicamos
# en el método init
alumno1 = Alumno("Iván", 8)
alumno2 = Alumno("Juan", 5)


# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
