from machine import Pin  

import time            

ldr = machine.ADC(27)  # Inicializa un convertor analogico-digital para pin 27

while True:

    luz_ambiental = ldr.read_u16()
    print("LDR Value:", luz_ambiental)
    if luz_ambiental > 0 and luz_ambiental < 5000:
        print("Hay mucha luz")
    if luz_ambiental > 5000 and luz_ambiental <15000:
        print("Luz moderada")
    if luz_ambiental > 15000 and luz_ambiental < 25000:
        print("Hay poca luz")
    if luz_ambiental > 25000:
        print("No hay luz")
        
    time.sleep(1.5)