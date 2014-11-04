import cv2

__author__ = 'esenin'


def open_image(path):
    img = cv2.imread(path, 0)
    print "image shape: ", img.shape
    return img


def show_image(img):
    cv2.imshow("Display . . .", img)
    cv2.moveWindow("", 1, 1)
    cv2.imwrite("task2_output.png", img)


def wait_exit():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def perform_changes_task2(img):
    cv2.GaussianBlur(img, (3, 3), 0, img)
    cv2.Laplacian(img, 0, img, 1)
    cv2.GaussianBlur(img, (19, 3), 7, img)
    cv2.threshold(img, 10, 255, cv2.THRESH_BINARY, img)
    #cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 5, img)
    return img


def main():
    img = open_image('text.bmp')
    e1 = cv2.getTickCount()

    img = perform_changes_task2(img)

    e2 = cv2.getTickCount()
    time = (e2 - e1) / cv2.getTickFrequency()

    show_image(img)
    print "time elapsed: ", time
    wait_exit()


main()
