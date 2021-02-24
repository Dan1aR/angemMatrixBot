import cv2
import numpy as np
from copy import copy
import pytesseract

class Scan:
    imgPath = None
    img = None
    matrix = None

    def __init__(self, ip):
        self.imgPath = ip

    def balance(self):
        img = cv2.imread(self.imgPath)
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #blackAndWhiteImage = cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        
        # Вырезаем картинку
        heigth, width, channels = img.shape
        minS = 10**10; maxS = 0
        prev = 0; startH = -1
        endH = heigth
        for i in range(1, heigth-1):
            if i > 0:
                s = 0
                for j in range(1, width-1):
                    s += (255-blackAndWhiteImage[i-1][j])
                prev = s
            s = 0
            for j in range(1, width-1):
                s += (255-blackAndWhiteImage[i][j])
            if s < minS and s != 0:
                minS = s
            if s > maxS:
                maxS = s
            if (s > 0) & (startH == -1):
                startH = i
            if (s == 0) & (prev > 0):
                endH = i            
        prev = 0; startW = -1; endW = width
        for i in range(1, width-1):
            if i > 0:
                s = 0
                for j in range(1, heigth-1):
                    s += (255-blackAndWhiteImage[j][i-1])
                prev = s
            s = 0
            for j in range(1, heigth-1):
                s += (255-blackAndWhiteImage[j][i])
            if (s > 0) & (startW == -1):
                startW = i
            if (s == 0) & (prev > 0):
                endW = i
        crop_img = blackAndWhiteImage[startH:endH, startW:endW]

        #Делаем пожирнее
        heigth = endH-startH; width = endW-startW
        for i in range(2, heigth):
            for j in range(2, width):
                if crop_img[i][j] == 0:
                    crop_img[i][j-1] = 0
                    crop_img[i][j-2] = 0
                    crop_img[i-1][j] = 0
                    crop_img[i-1][j-1] = 0
                    crop_img[i-1][j-2] = 0
                    crop_img[i-2][j] = 0
                    crop_img[i-2][j-1] = 0
                    crop_img[i-2][j-2] = 0
        

        cv2.imshow("img", crop_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.img = crop_img
    
    def getMatrixIMG(self):
        img = self.img
        custom_config = r'--oem 3 --psm 6'
        heigth, width = img.shape
        matrix = [[]]

        line1, line2 = 0, 0
        idx = 0
        prev = 0
        while line2 < heigth:
            s = 0
            for i in range(width):
                s += 255-img[line2][i]
            
            if s < 8000 and prev > 8000:
                crop = img[line1:line2]
                col1, col2 = 0, 0
                prevC = 0
                while col2 < width:
                    sc = 0
                    for i in range(line2-line1):
                        sc += 255-crop[i][col2]
                    if sc < 511 and prevC > 511:
                        cropC = crop[:, col1:col2]
                        
                        #Начать распознавать туть
                        #КАКАЯ ЖЕ ХУЙНЯ!!!!
                        cv2.imshow("c", cropC)
                        cv2.waitKey(0)
                        ocr_result = pytesseract.image_to_string(cropC, config='--psm 10 --oem 3 -c tessedit_char_whitelist=-0123456789')
                        print(ocr_result)

                        #matrix[idx] += [numeric!!!]
                        col1 = copy(col2)
                    prevC = copy(sc)
                    col2 += 1
                    
                line1 = copy(line2)
                idx += 1
                matrix += [[]]

            prev = copy(s)
            line2 += 1

    def getMatrix(self, s):
        matrix = []
        s = s.split("\n")
        for sin in s:
            matrix += [list(map(float, sin.split()))]
        self.matrix = matrix

    
myScan = Scan('/home/dan1ar/Рабочий стол/Python/angemBOT/toScan/1.jpg')
myScan.balance()
myScan.getMatrixIMG()