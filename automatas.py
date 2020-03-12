#AUTOMATAS

#Aut letras

def letras(cadena):
    estado=1
    for i in range(0, len(cadena)):
        actual=cadena[i]

        if estado == 1:
            if str.isalpha(actual):
                estado = 2
            else:
                return False
        elif estado == 2:
            if str.isalpha(actual):
                estado=2
            else:
                return False
    if estado == 2:
        return True
    else:
        return False



#Aut Numeros

def numeros(cadena):
    estado=1
    for i in range (0, len(cadena)):
        actual=cadena[i]

        if estado == 1:
            if str.isdigit(actual):
                estado=2
            else:
                return False
        elif estado == 2:
            if str.isdigit(actual):
                estado=2
            else:
                return False
    if estado==2:
        return True
    else:

        return False


#Aut Numeros hasta el 5
#E: un caracter
#S: un bool
    
#NOTA: Evalua solo un caracter, si de entrada tiene que ir una cadena , hay que hacerlo diferente(con FOR)

def numeros_5(caracter):
    estado=1
    if numeros(caracter):
        num=int(caracter)
        if 6>num>=0:
            estado=2
            return True 
        else:
             return False
        
                  
    else:
         return False




#Aut de letras hasta la F
#E: un caracter
#S: un bool
#D: Compara que el caracter este dentro de la lista de letras de la A a la F
# evalua tanto mayusculas como minusculas
        
def letras_F(caracter):
    
    estado=1
    if letras(caracter):
        listaLetras=["A","B","C","D","E","F","a","b","c","d","e","f"]
        if caracter in listaLetras:
            estado==2
            return True
        else:
            return False
        



    return False


#Aut de Valor hexadecimal
#E: una cadena
#S: un bool

def hexadecimal(cadena):

    if cadena[0]=="0" and cadena[1]=="x":
        estado=1
        for i in range (2, len(cadena)):
            actual=cadena[i]
            
            if estado == 1:
                if numeros(actual) or letras_F(actual):
                    estado=2
                else:
                    return False
            elif estado == 2:
                if numeros(actual) or letras_F(actual):
                    estado=2
                else:
                    return False
                        

        if estado==2:
            return True

    return False
    


















        
                
