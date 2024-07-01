/*
	A pesar de que este proyecto se dejó por el de la PyBike, he de mencionar que el código
    presente lo sacamos de la página https://www.instructables.com/ y del siguente artículo escrito
    por el usuario "cryp7o" en la misma página: 
    https://www.instructables.com/LDR-Light-Sensor-on-Raspberry-Pi-Pico/
    Nosotros tomamos este código y lo modificamos para nuestro uso en específico.
*/

from machine import Pin  
import time            

ldr = machine.ADC(27) 

while True:

    ldr_value = ldr.read_u16() 
    print("LDR Value:", ldr_value)  
    luz=ldr_value
    if luz < 25000:
        print("Hay luz")
    else:
        print("No hay luz")
        
    time.sleep(1.5)
