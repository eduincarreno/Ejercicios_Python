import user
import passw
print("Bienvenido al módulo de usuario")
print("Vamos a crear tú usuario")
correcto=False
while correcto==False:
        nombre=input("Ingrese un usuario: ")
        if user.validar_usuario(nombre) == True:
            print("El usuario se creó exitosamente")
            correcto=True
print("Ahora vamos a crear tú contraseña")
while correcto==True:
    cont=input("Ingresa una Contraseña: ")
    if passw.password(cont)==True:
        print("Tú contraseña se creó exitosamente")
        correcto=False