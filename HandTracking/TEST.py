import  glob
import cv2
path = glob.glob("E:\Python\HandTracking\Data\*.png")
for file in path:
    img = cv2.imread(file)
    cv2.imshow("Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()