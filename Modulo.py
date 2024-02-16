import json

def añadirUsuario():
    with open('usuarios.json','r') as archivo:
        data = json.load(archivo)
    usuario = data['Usuario']
    nuevo_usuario = {}
    nuevo_usuario['identidad'] = int(input('Ingresa el numero de identidad: '))
    nuevo_usuario['nombre'] = input('Ingresa el nombre del usuario: ')
    nuevo_usuario['apellido'] = input('Ingresa el apellido del usuario: ')
    nuevo_usuario['direccion'] = input('Ingrese la direccion del usuario: ')
    nuevo_usuario['celular'] = int(input('Ingresa el numero de contacto del usuario: '))
    nuevo_usuario['año'] = int(input('Ingresa el año de cuando ingreso el usuario: '))
    nuevo_usuario['categoria'] = ''
    

    usuario.append(nuevo_usuario)
    
    with open('usuarios.json','w') as archivo:
        json.dump(data,archivo,indent=4)
        
#añadirUsuario()

def buscarUsuario():
    with open('usuarios.json','r') as archivo:
        data = json.load(archivo)
    usuario = data['Usuario']
    id_usuario  = int(input('Ingrese el numero de identidad del usuario que desea buscar: '))

    for usuari in usuario:
        if usuari['identidad'] == id_usuario:
            print(usuari)

#buscarUsuario()

def ActualizarUsuario():
    with open('usuarios.json','r') as archivo:
        data = json.load(archivo)
    usuario = data['Usuario']
    id_usuario = int(input('Ingrese el numero de identidad del usuario que desea actualizar: '))
    
    for usuari in usuario:
        if usuari['identidad'] == id_usuario:
            usuari['identidad'] = int(input('Ingresa el nuevo numero de identidad: '))
            usuari['nombre'] = input('Ingresa el nuevo nombre del usuario: ')
            usuari['apellido'] = input('Ingresa el nuevo apellido del usuario: ')
            usuari['direccion'] = input('Ingresa la nueva direccion del usuario: ')
            usuari['celular'] = int(input('Ingrese el nuevo numero de contacto: '))
            usuari['año'] = int(input('Ingrese el nuevo año de ingreso: '))
            usuari['categoria'] = ''
    with open('usuarios.json','w') as archivo:
        json.dump(data,archivo,indent=4)

#ActualizarUsuario()

def eliminarUsuario():
    with open('usuarios.json','r') as archivo:
        data = json.load(archivo)
    usuario = data['Usuario']
    id_usuario = int(input('Ingrese el numero de identidad del usuario que desea eliminar: '))

    for usuari in usuario:
        if usuari['identidad'] == id_usuario:
            usuario.remove(usuari)

    with open('usuarios.json','w') as archivo:
        json.dump(data,archivo,indent=4)

#eliminarUsuario()

def Categoria():
    with open('usuarios.json','r') as archivo:
        data = json.load(archivo)
    usuario = data['Usuario']
    
    
    for usuari in usuario:
        if usuari['año'] <= 2014:
            usuari['categoria'] = 'cliente Fiel'
        elif usuari['año'] > 2014 and usuari['año'] <= 2019:
            usuari['categoria'] = 'cliente regular'
        else:
            usuari['categoria'] = 'cliente nuevo'
        
    with open('usuarios.json','w') as archivo:
        json.dump(data,archivo,indent=4)

#Categoria()

def AñadirServicio():
    with open('servicios.json','r') as archivo:
        data = json.load(archivo)
    
    servicios = data['Servicios']
    servicios2 = input('Ingresa un servicio: ')
    nuevo_servicios = {}
    nuevo_servicios[servicios2] = {}
    
    
    servicios.append(nuevo_servicios)
    
    with open('servicios.json','w') as archivo:
        json.dump(data,archivo,indent=4)

#AñadirServicio()

def EliminarServicios():
    with open('servicios.json','r') as archivo:
        data = json.load(archivo)
    servicios = data
    num = input('Ingresa el nombre del servicio que deseas eliminar: ')
    for servicio in servicios:
        if servicio == num:
            servicios.remove(servicio)
    
    with open('servicios.json','w') as archivo:
        json.dump(data,archivo,indent=4)

EliminarServicios()            
            
    
    
        



