Contador de Dedos con Python y Arduino
Este proyecto tiene como objetivo desarrollar un sistema de visión por computadora que detecta la cantidad de dedos levantados utilizando la librería MediaPipe en Python y envía esa información a un Arduino. En el lado de Arduino, los LEDs se encienden para simular una suma acumulativa basada en el número de dedos detectados.

Descripción del Proyecto
Se utiliza Python con la librería MediaPipe para el seguimiento de la mano y el conteo de los dedos.

OpenCV se utiliza para visualizar el video en tiempo real y mostrar la cantidad de dedos detectados.

El número de dedos detectados se envía al Arduino a través del puerto Serial (USB).

En el Arduino, el número de dedos levantados se refleja mediante el encendido de dos LEDs.

Componentes Requeridos

Hardware:
Placa Arduino UNO/Nano (o similar)

2 LEDs (uno para cada dedo detectado)

Resistencias para los LEDs (220Ω o similar)

Cables jumper

Protoboard (opcional, pero recomendado para una mejor organización de los componentes)

Software:
Python 3.x


Esquema del Circuito:
El circuito está compuesto por dos LEDs conectados al Arduino de la siguiente manera:

LED 1: Conectado al pin 13 del Arduino.

LED 2: Conectado al pin 12 del Arduino.

Ambos LEDs deben estar conectados con una resistencia de 220Ω en serie para evitar sobrecargar los pines.

El código de Arduino se encarga de encender los LEDs dependiendo de la cantidad de dedos levantados. Si el número de dedos es 1, se enciende el primer LED; si el número de dedos es 2, ambos LEDs se encienden.

Código de Python
Este es el código Python que utiliza OpenCV y MediaPipe para detectar los dedos levantados y enviar esta información al Arduino a través de la comunicación Serial.


Instrucciones para Ejecutar el Proyecto:
Conecta tu Arduino a tu computadora mediante el cable USB.

Carga el código de Arduino en tu placa Arduino utilizando el Arduino IDE.


VIDEO EXPLICATIVO DEL PROYECTO: https://youtu.be/f6WVYAnsxqQ

