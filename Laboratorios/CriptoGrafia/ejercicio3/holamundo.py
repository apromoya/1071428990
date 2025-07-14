
def holamundo():
    print('Ingresar nombre: ')
    nombres = input()

    print('Ingresar Apellido: ')
    apellidos = input()

    datos = 'Vayase de aqui señor ' + nombres + ' ' + apellidos

    print('Informacion: ' + datos)
    return None

if __name__ == '__main__':
    holamundo()