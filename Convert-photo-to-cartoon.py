# Generat by  AmiraliZandi 
#    ===                             =                 ===      ==       =
#  =     =   ==   ===      ===             ==   =    =     =    ==  
#  =======   ==  =   =   =    =     ==     == =      =======    ==       ==
#  =     =   == =     = =      =    ==     ==        =     =    ==       ==
#  =     =   ==        =       =    ==     ==        =     =    ======   ==

#**************************************************************************************************
import cv2
import numpy as np


def cartoonize_image(image):
   
    filtered = cv2.bilateralFilter(image, 9, 250, 250)

    
    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY)


    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 2)

    
    color = cv2.bilateralFilter(image, 8, 250, 250)


    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon



image = cv2.imread("your image")
cartoonized = cartoonize_image(image)


cv2.imshow("Cartoonized Image", cartoonized)
cv2.waitKey(0)
cv2.destroyAllWindows()
