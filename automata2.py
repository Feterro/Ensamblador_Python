#numeros con 0
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

#letras y "_" hola
def letras(cadena):
    estado=1
    for i in range(0, len(cadena)):
        actual=cadena[i]

        if estado == 1:
            if str.isalpha(actual) or actual == "_":
                estado = 2
            else:
                return False
        elif estado == 2:
            if str.isalpha(actual) or actual == "_":
                estado=2
            else:
                return False
    if estado == 2:
        return True
    else:
        return False

#numeros y letras con espacios
def caracter(cadena):
    estado=1
    for i in range(0, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False
            
        elif estado == 2:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False

        elif estado == 3:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False

        elif estado == 4:
            if numeros(actual):
                estado = 2
            elif letras(actual):
                estado = 3
            elif actual == " ":
                estado = 4
            else:
                return False

            
    if estado == 2 or estado == 3 or estado == 4:
        return True
    else:
        return False

#.program
def program(cadena):
    estado = 1

    for i in range(0, len(cadena)):
        actual = cadena[i]

        if estado == 1:
            
            if actual == '.':
                estado = 2
            else:
                return False
        
        elif estado == 2:
            if actual == 'p':
                estado = 3
            else:
                return False
            
        elif estado == 3:
            if actual == 'r':
                estado = 4
            else:
                return False
            
        elif estado == 4:
            if actual == 'o':
                estado = 5
            else:
                return False
            
        elif estado == 5:
            if actual == 'g':
                estado = 6
            else:
                return False
            
        elif estado == 6:
            if actual == 'r':
                estado = 7
            else:
                return False
            
        elif estado == 7:
            if actual == 'a':
                estado = 8
            else:
                return False
        elif estado == 8:
            if actual == 'm':
                estado = 9
            else:
                return False
            
        elif estado == 9:
            if actual == " ":
                estado = 10
            else:
                return False
            
        elif estado == 10:
            if caracter(actual):
                estado == 10
            else:
                return False

            
    if estado == 10:
        return True
    else: return False

def main():
    cadena=".program Este es_mi_primer111programa"
    if program(cadena)==True:
        print("Yaaasss")
    else:
        print("F")


main()
