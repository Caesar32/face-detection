# Real time face detection using opencv

import cv2
import cvzone.FaceDetectionModule  

# Lanch the live camera
cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    #Check camera
    if not cap.isOpened():
        print("Camera not working")
        break

    # Get image frame
    success, img = cap.read()

    img, bboxs = detector.findFaces(img)

    # Display webcam
    cv2.imshow("Image", img)

    # Press ESC or q to close or terminate the while loop
    key= cv2.waitKey(10)
    if key==27 or key==ord('q'):
        break
    # if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) == 27:
    #     break

cap.release()
cv2.destroyAllWindows()