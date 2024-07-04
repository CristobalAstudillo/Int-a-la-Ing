# Proyecto PyBike V1.5
Hecho por:
- Cristobal Astudillo
    * Rol Usm: 20243013-K
- Francisco Bugueño
    * Rol Usm: 202430014-8
- Lucas Verdejo
    * Rol Usm: 202430
- Patricio Celis
    * Rol Usm: 202430

## Pequeña Introducción
Nosotros somos un grupo de alumnos de [Universidad Federico Santa María](https://usm.cl/) que está cursando su primer año de la carrera [Ingeniería civil Telemática](https://usm.cl/admision/carreras/ingenieria-civil-telematica/).
Para este ramo en específico, Introducción a la Ingeniería, teníamos que hacer un analísis de nuestro entorno, buscar problemáticas y resolverlas. En un principio, modificamos un calculadora para que cuando haya ausencia de luz, esta
se apagara por si sola ya que habíamos detectado que se demoraban mucho en hacerlo. Dadas ciertas situaciones que describiremos más adelante, decidimos cambiar el proyecto a modificar una bicicleta, llamada "PyBike", que fue un proyecto de otros estudiantes en años anteriores. 
## De una calculadora a una bicicleta
Como dijimos antes, nosotros teníamos cómo proyecto el modificar una calculadora, la cual, en ausencia de luz, se apagara. Esto porque habíamos detectado que, por si solas, se demoraban mucho en 
apagarse y queríamos alargar la vida útil de la pila que se encuentra en estas. Presentamos esto como avance y, nuestro profesor, [Werner Creixell](https://www.linkedin.com/in/creixell/?locale=es_ES), no nos dijo que estaba malo, pero si que
le teníamos que dar otra perspectiva.

Decimos descartar la idea y empezar desde cero. Aún así, a pesar de que la mencionada calculadora modificada no fue nuestro proyecto final,
dejaremos el código, y todas sus versiones, [acá](https://github.com/lilcrixx01/Int-a-la-Ing/tree/main/Calculadora).

## De PyBike a PyBike V1.5
La idea de modificar la PyBike vino de Patricio Celis, ya que él se enteró, hablando con alumnos de años superiores, que este proyecto de años anteriores existía y que, además, la podíamos modificar y que la modifición y renovación de esta podía ser nuestro proyecto para el ramo.

Desde el principio que teníamos claro que tipo de modificaciones le vendrían bien, no solo a la PyBike, sino que a cualquier bicicleta:

- Existen señas que el conductor del ciclo puede realizar mientras conduce para indicar si va a girar a la derecha o a la izquierda, pero estas señas involucran no tener ambos manos en el volante. Entonces, decimos usar una [**matriz de leds de tamaño 8x8**](https://afel.cl/producto/matriz-de-leds-8x8-max-7219/) y unos botones, izquierda y derecha, para que cuando el conductor presione uno de estos botones en la matriz de leds se muestre una **_flecha en movimiento correspondiente al botón pulsado_**. Eliminando así la necesidad de las señas y asegurarse de que el conductor del ciclo tenga las dos manos en el volante.

- Aprovechando la matriz de leds, y el código que teníamos del descartado proyecto de la calculadora, decidimos añadir algo que, he de reconocer, es una modificación que uno ya puede comprar, que es una [**luz trasera para la bicicleta**](https://listado.mercadolibre.cl/luz-trasera-bicicleta).

  Comentando entre nosotros, dicidimos que no era necesario que la luz estuviera prendida todo el tiempo, dado que ha plena luz del día no era       necesario, pero si era necesario cuando hubiera poca o ausencia de luz. Asi que, usando una [**fotoresistencia**](https://www.mechatronicstore.cl/fotoresistencia-ldr-5mm/) hicimos que, cuando haya poca o ausencia de luz, se prendieran todos los leds de la       matriz para que así los autos puedan saber que ahí hay una bicicleta. Esta idea tambíen surgió dado que, lamentablemente, los conductores de       ciclo, o al menos la mayoría, *_no ocupa chalecos reflectantes en situaciones de escasa luz_*.

Aparte de estas dos ideas principales, nuestro compañero Francisco, tuvo una idea que tambíen podríamos montar un [**sensor ultrasónico**](https://afel.cl/producto/sensor-de-ultrasonico-hc-sr04/) y un [**buzzer**](https://maxelectronica.cl/prototipo/293-buzzer-zumbador-activo-5-volts.html) en la parte de atrás del ciclo para que actuara cómo un sensor de proximidad para que el conductor estuviera más conciente de su alrededor.

## Modificación

Teniendo las ideas claras, nos pusimos manos a la obra. Antes de instalar todo en el bicicleta tuvimos que hacer dos cosas:

- Hicimos pruebas utilizando una placa [**arduino UNO**](https://arduino.cl/producto/arduino-uno/) y una [**protoboard**](https://arduino.cl/producto/protoboard-de-tamano-completo-830pts-mb-102/) fuera de la bicicleta para saber que nuestro código funcionaba y que el hardware no tuviera problemas.
- Dado el estado en el cual estaba la PyBike y el corto período de tiempo que teníamos, tuvimos que desmantelar la mayoría de la PyBike original. Esto por la mencionada falta de tiempo y además, nuestros conocimientos no son tan vastos cómo para ambos proyectos funcionaran en conjunto.

Una vez desmantelada la antigua PyBike, trasladamos lo que teníamos en la **protoboard** a bicicleta. Resultando en un proyecto funcional, pero *_completamente mejorable tanto en el área estética cómo práctica_*.

### Código Originales


