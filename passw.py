def password(passw):

        validar=False
        longitud=len(passw)
        espacio=False
        mayuscula=False
        minuscula=False
        numeros=False
        revisar =passw.isalnum()
        correcto=True

        for carac in passw:

            if carac.isspace()==True:
                espacio=True

            if carac.isupper()== True:
                mayuscula=True

            if carac.islower()== True:
                minuscula=True

            if carac.isdigit()== True:
                numeros=True

        if espacio==True:
                print("La contraseña no puede contener espacios")
        else:
            validar=True

        if longitud <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False

        if mayuscula == True and minuscula ==True and numeros == True and revisar == False and validar ==True:
           validar = True
        else:
           correcto=False

        if validar == True and correcto==False:
           print("La contraseña no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")

        if validar == True and correcto ==True:
           return True