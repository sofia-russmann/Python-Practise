# rebotes.py
# Archivo de ejemplo
# Ejercicio


cant_salto = 1
altura = 100
altura_final = 0


while cant_salto<=10:
    cant_salto = cant_salto + 1
    altura_final = 3/5 * altura
    altura = altura_final
    print(round(altura, 4))
    
