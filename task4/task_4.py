__author__ = 'esenin'

import cv2
import numpy as np


def open_image(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print "image shape: ", img.shape
    return img


def wait_exit():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_image(img, orig):
    cv2.imwrite("task4_result.png", img)

    shift_y = 50
    shift_x = 50
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow("img", img)
    cv2.moveWindow("img", shift_x, shift_y)
    imshape = img.shape

    cv2.namedWindow('origi', cv2.WINDOW_NORMAL)
    cv2.imshow("origi", orig)
    cv2.moveWindow("origi", shift_x + imshape[1], shift_y)


def high_freq_filter(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 0.07 * np.log(np.abs(fshift))

    rows, cols = img.shape
    radius = rows / 3
    crow, ccol = rows/2, cols/2
    fshift[crow-radius:crow+radius, ccol-radius:ccol+radius] = 0

    # fshift[0:radius, 0:radius] = 0
    # fshift[rows-radius:rows, 0:radius] = 0
    # fshift[0:radius, cols-radius:cols] = 0
    # fshift[rows-radius:rows, cols-radius:cols] = 0

    img_back = np.fft.ifft2(np.fft.ifftshift(fshift))
    img_back = 0.005 * np.abs(img_back)

    return img_back


def main():
    img = open_image('mandril.bmp')
    orig = img.copy()
    e1 = cv2.getTickCount()

    img = high_freq_filter(img)

    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()

    show_image(img, orig)
    print "time elapsed: ", time
    wait_exit()



main()