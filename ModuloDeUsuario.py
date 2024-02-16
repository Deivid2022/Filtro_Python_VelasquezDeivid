import json

def añadirUsuario():
    with open('usuarios.json','r') as archivo:
        data = json.load(archivo)
    usuario = data['Usuario']

    nuevo_usuario = {}
    nuevo_usuario['nombre'] = input('Ingresa el nombre del usuario: ')
    nuevo_usuario['apellido'] = input('Ingresa el apellido del usuario: ')
    nuevo_usuario['direccion'] = input('Ingrese la direccion del usuario: ')
    nuevo_usuario['celular'] = input('Ingresa el numero de contacto del usuario: ')

    nuevo_usuario.append(usuario)
    