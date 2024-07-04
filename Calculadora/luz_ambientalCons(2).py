from machine import Pin
import time

mucha_luz=5000
luz_moderada=15000
poca_luz=25000               
no_luz=25001                
        
ldr = machine.ADC(27)  

while True:

    luz_ambiental = ldr.read_u16() 
    print("LDR Value:", luz_ambiental)  
    
    if luz_ambiental < mucha_luz:
        print("Hay mucha luz")
    if luz_ambiental > mucha_luz and luz_ambiental < luz_moderada:
        print("Luz moderada")
    if luz_ambiental > luz_moderada and luz_ambiental < poca_luz:
        print("Hay poca luz")
    if luz_ambiental >= no_luz:
        print("No hay luz")
        
    time.sleep(1.5)
