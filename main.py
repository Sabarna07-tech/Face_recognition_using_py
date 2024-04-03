import threading
import cv2
from deepface import DeepFace
# devices = cv2.VideoCapture.getDeviceList()
device_id = 0
cap = cv2.VideoCapture(device_id, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img = cv2.imread("WhatsApp Image 2024-03-14 at 21.36.31_2a77e5de.jpg")
def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:

        face_match= False

while True:
    ret, frame = cap.read()
    if ret:
        if counter %30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass
        counter +=1
        if face_match:
            cv2.putText((frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2,(0, 255, 0), 3))
        else:
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            cv2.imshow("video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
