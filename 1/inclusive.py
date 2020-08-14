#frase = 'todos somos programadores'
#frase = 'Los hermanos sean unidos porque esa es la ley primera'
frase = 'Cómo transmitir a los otros el infinito Aleph?'
#frase = 'Todos, tu también'

palabras = frase.split()

i1 = -1
i2 = -2
#i3 = -3

frase_t = ''

for palabra in palabras:
    if len(palabra) >= 2:
        if palabra[i1] == 'o':
            palabra = palabra[:i1] + 'e' 
        elif palabra[i2] == 'o' :
            palabra = palabra[:i2] + 'e' + palabra[i2+1:]
        #elif palabra[i1] == ',' and  palabra[i2] == 'o':
            #palabra = palabra[:i2] + 'e' + palabra[i2+1:]
        #elif palabra[i1] == ',' and  palabra[i3] == 'o':
            #palabra = palabra[:i3] + 'e' + palabra[i3+1:]

    frase_t += ' ' + palabra 
    
print(frase_t)   



#Trabajando en el bug para i=','