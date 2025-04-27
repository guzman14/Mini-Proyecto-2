import cv2
import mediapipe as mp
import serial
import time

# Configurar el puerto serial (ajusta el puerto, por ejemplo: COM3 o /dev/ttyUSB0)
arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Esperar que el Arduino inicie

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Abrir la cámara
cap = cv2.VideoCapture(0)

# Para controlar cambios de número
prev_count = -1

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((lm.x, lm.y))

            # Detección simple de dedos levantados
            if lm_list:
                # Pulgar
                if lm_list[4][0] < lm_list[3][0]:
                    count += 1
                # Otros 4 dedos
                for tip_id in [8, 12, 16, 20]:
                    if lm_list[tip_id][1] < lm_list[tip_id - 2][1]:
                        count += 1

            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Enviar solo si el conteo cambió
    if count != prev_count:
        arduino.write(str(count).encode())
        prev_count = count
        print(f"Dedos detectados: {count}")

    # Mostrar imagen
    cv2.imshow("Contador de Dedos", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
arduino.close()
