import cv2
import numpy as np

imgRisqi = cv2.imread('Risqi.jpg')
grayRisqi = cv2.cvtColor(imgRisqi, cv2.COLOR_RGB2GRAY)

grayRisqi_3_channel = cv2.cvtColor(grayRisqi, cv2.COLOR_GRAY2BGR)
image_show = np.hstack((imgRisqi, grayRisqi_3_channel))
cv2.imshow('Hasil Citra RGB Menjadi Gray Scale', image_show)
cv2.waitKey()