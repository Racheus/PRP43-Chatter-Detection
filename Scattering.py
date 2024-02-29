import os
import cv2
cnt = 0
for file_name in os.listdir('CWTImage'):
    img = cv2.imread('CWTImage/' + file_name)
    x1, y1 = 125, 75  # 左上角坐标
    x2, y2 = 745, 535  # 右下角坐标
    img = img[y1:y2, x1:x2]
    cv2.imwrite('PureCWTImage/' + file_name, img)
    print('Picture ' + str(cnt) + ' has been processed')
    cnt+=1

