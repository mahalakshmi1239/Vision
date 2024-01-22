import cv2
vid = cv2.Vedio.Capture(0)
result,image = vid.read(),
if result:
    cv2.inshow("IMAGE",image)
    cv2.inwrite(siri.png",image)
while(True):
    _,frame=vid.read()
    cv2.inshow("frame",frame)
    if cv2.waitkey(1)& OxFF==ord("q"):
        break
vid.release()
cv2.destroyAllWindows()

