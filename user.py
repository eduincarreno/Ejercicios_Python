  
def validar_usuario(nombre_usuario):

     longitud=len(nombre_usuario)
     nameuser=nombre_usuario.isalnum()

     if nameuser== False:
         print("El usuario debe tener letras y números")

     if longitud < 6:
         print("El usuario debe contener mínimo 6 caracteres")

     if longitud > 12:
         print("El usuario debe contener máximo 12 caracteres")

     if longitud >5 and longitud <13 and nameuser ==True:
        return True
