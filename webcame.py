
import cv2
cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,980)
cap.set(10,100)
while True:
  success,img =cap.read()
  if not success:
        break
  cv2.imshow("webcam",img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
