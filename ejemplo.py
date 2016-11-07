#archivo de lectura
archivo = open ("documento.txt","r")
#archivo de escritura
archivo2 = open("prueba.txt",'w')

contador= 0;
espacio = " "

for linea in archivo:

    for letras in linea:
        if letras == 'a':
            archivo2.write(espacio)

        elif letras == 'e':
        	archivo2.write(espacio)

        elif letras == 'i':
        	archivo2.write(espacio)

        elif letras == 'o':
        	archivo2.write(espacio)

        elif letras == 'u':
        	archivo2.write(espacio)

        else:
 		    archivo2.write(letras)



print "archivo creado"
archivo.close()
archivo2.close()

