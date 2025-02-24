#ejercicio 12
import os
cantidad=0
contactos=[]
def agregar_contacto():
    contactos.append(diccionario)
for c in (1, cantidad+1):   
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
    agregar_contacto()
    print(f'la lista de contactos ha sido actualizada: {contactos}')
    respuesta=input('desea agregar otro contacto? s/n\n').lower()
    if respuesta == 's' or respuesta=='si':
       pass
    else:
        print('hasta luego...')
        break
        