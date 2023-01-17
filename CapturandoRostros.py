import cv2
import os
import imutils
import time

emotionList = [
    'Enojo',
    'Felicidad',
    'Sorpresa',
    'Asco',
    'Miedo',
    'Tristeza',
    'Desprecio',
]

dataPath = f'{os.getcwd()}/Data'  # Cambia a la ruta donde hayas almacenado Data

for emotionName in emotionList:
    emotionsPath = dataPath + '/' + emotionName

    if not os.path.exists(emotionsPath):
        separador = "=" * (len(str(emotionsPath)) + 17)
        print(f"{separador}\nCarpeta creada: {emotionsPath}\n{separador}")
        os.makedirs(emotionsPath)

        seconds = 5
        while True:
            print(f"*********** ABRIENDO CAMARA EN {seconds} **********")
            if seconds == 0: break
            seconds -= 1
            time.sleep(1)
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        count = 0

        while True:

            ret, frame = cap.read()
            if ret == False: break
            frame = imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()

            faces = faceClassif.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                rostro = auxFrame[y:y + h, x:x + w]
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(emotionsPath + '/rostro_{}.jpg'.format(count), rostro)
                count = count + 1
            cv2.imshow('frame', frame)

            k = cv2.waitKey(1)
            if k == 27 or count >= 200:
                print(f"\n --- Se capturaron {count}  frames ---")
                break

        cap.release()
        cv2.destroyAllWindows()
