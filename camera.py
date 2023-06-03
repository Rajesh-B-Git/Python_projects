# install pip install opencv-contrib-python package
# Program capture video from mobile cam
import cv2

cap = cv2.VideoCapture(0)
address = "https://192.168.1.6:8080/video"
cap.open(address)

while (True):
    ret, frame = cap.read()

    cv2.imshow('Frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    if cv2.waitKey(33) == ord('a'):
        cv2.imwrite('image.png', frame)


cap.release()
cv2.destroyAllWindows()
