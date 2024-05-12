from machine import Pin  
import time            

ldr = machine.ADC(27) 

while True:

    ldr_value = ldr.read_u16() 
    print("LDR Value:", ldr_value)  
    luz=ldr_value
    if luz < 20000:
        print("Hay luz")
    else:
        print("No hay luz")
        
    time.sleep(1.5)
