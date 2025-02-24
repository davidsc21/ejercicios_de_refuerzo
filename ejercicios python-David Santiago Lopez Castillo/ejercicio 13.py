#ejercicio 13
import os
cantidad=0
contactos=[]
def mostrar_contacto(contactos):
    filtro=input('ingrese nombre del contacto:\n').lower()
    for contacto in contactos:
            if filtro in contacto['nombre'].lower():
                print(f'nombre: {contacto["nombre"]}, telefono: {contacto["telefono"]}')
while True:    
    respuesta=input('Bienvenido usuario que desea hacer:\n1.crear nuevo contacto\n2.bucar contacto\n3.salir\n')
    match respuesta:
        case '1':    
            while True:   
                nombre=input('ingrese el nombre del nuevo contacto:\n')
                while True:    
                    try:
                        telefono=(int(input('ingrese el numero del contacto:\n')))
                        break
                    except  ValueError:
                        print('ingrese un valor valido')
                diccionario={
                    'nombre':nombre,
                    'telefono' : telefono,
                }
                contactos.append(diccionario)
                respuesta=input('desea agregar otro contacto? s/n\n').lower()
                if respuesta not in ('s','si'):
                    print('volviendo al menu principal')
                    break                  
        case '2':
                mostrar_contacto(contactos)
                pause = input("")
        case '3':
            print('hasta luego...')
            break
            