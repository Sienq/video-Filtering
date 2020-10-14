import cv2
import numpy as np
def customEdgeDetection(ksize,img):

    if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
        print("not valid ksize, both numbers must be odd")
        return
    else:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kernel = np.full(ksize,-1)
        kernel[int(ksize[0])//2,int(ksize[0])//2] = (int(ksize[0])**2) - 1
        print(kernel)
        cv2.filter2D(img,-1,kernel,img)
        return img

def customSharpen(ksize,img):

    if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
        print("not valid ksize, both numbers must be odd")
        return
    else:
        kernel = np.full(ksize,-1)
        kernel[int(ksize[0])//2,int(ksize[0])//2] = (int(ksize[0])**2)
        print(kernel)
        cv2.filter2D(img,-1,kernel,img)
        return img

def customBlur(ksize,img):

    if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
        print("not valid ksize, both numbers must be odd")
        return
    else:
        kernel = np.full(ksize,1.0/int(ksize[0])**2)
        print(kernel)
        cv2.filter2D(img,-1,kernel,img)
        return img


def customAsymethric(ksize,img):
        if int(ksize[0]) % 2 == 0 and int(ksize[1]) % 2 == 0 :
            print("not valid ksize, both numbers must be odd")
            return
        else:
            kernel = np.zeros(ksize)
            count = 1
            for i in range(int(ksize[0])):
                temp = -int(ksize[0]) + count
                for j in range(int(ksize[0])):
                    kernel[i,j] = temp
                    temp+=1
                count+=1
            cv2.filter2D(img,-1,kernel,img)
            return img


