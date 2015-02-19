#  computer vision, task 3, words detection
__author__ = 'esenin'

import cv2
import numpy as np


def open_image(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print "image shape: ", img.shape
    return img


def show_image(img, orig):
    cv2.imwrite("task3_output.png", img)
    cv2.imwrite("task3_onOrig.png", orig)

    shift_y = 70
    shift_x = 600
    cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
    cv2.imshow("img", img)
    cv2.moveWindow("img", shift_x, shift_y)
    (h, w) = img.shape

    cv2.namedWindow('onOrig', cv2.WINDOW_FREERATIO)
    cv2.imshow("onOrig", orig)
    cv2.moveWindow("onOrig", shift_x, shift_y + 2 * h)


def wait_exit():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_contours(pic, contours, color):
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(pic, (x, y), (x + w, y + h), color)
    return pic


def filter_words(img):
    orig = img.copy()
    cv2.Laplacian(img, 0, img, 1)

    kernel = np.ones((3, 5), np.uint16)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_ret, contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    (h, w) = img.shape
    new_value = 100
    mask = np.zeros((h + 2, w + 2, 1), np.uint8)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        seed_point = (x + 3 * w / 4, y + h / 2)
        cv2.floodFill(img, mask, seed_point, new_value)

    cv2.threshold(img, 30, 255, cv2.THRESH_BINARY, img)

    img_ret, post_contours, hierarchy = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = draw_contours(img, post_contours, 100)
    orig = draw_contours(orig, post_contours, (0, 0, 255))

    return img, orig


def main():
    img = open_image('../text.bmp')
    e1 = cv2.getTickCount()

    img, orig = filter_words(img)

    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()

    show_image(img, orig)
    print "time elapsed: ", time
    wait_exit()

main()