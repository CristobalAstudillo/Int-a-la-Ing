from machine import Pin
import time

poca_luz=20000
   
fotoR = machine.ADC(27)  #Pin en el cual está la fotoresistencia y del cual se va a leer la resistencia de esta.
calcu= Pin(26, Pin.OUT)  #Pin en el cual está conectada la calculadora y lo deja como un pin de salida

while True:
                                       # Lee el valor de la resistencia y lo convierte a un valor de 16 bits.
    luz_ambiental = fotoR.read_u16()   # Entre más luz incida en la superficie de la fotoresistencia
                                       # menor será el valor leído. Y si hay poca/nula luz incidiendo en la superficie, el valor leído será mayor.
    
    print("Valor de la fotoresistencia:", luz_ambiental)  # Imprime el valor que de la resistenia
    if luz_ambiental > poca_luz:
        calcu.value(0) #Si luz ambiental es mayor o igual al valor de 23k, apague el pin 26
    else:
        calcu.value(1) #Si luz ambiental es menor al valor de 23k, deje el pin prendido.
       
    time.sleep(1.5) #Repita todo lo anterior cada 1.5[s].
