import time

import cv2
import numpy as np


def get_from_file() -> np.array:
    img = cv2.imread("photo/20.jpg", 0)
    img = cv2.resize(img, (640, 480))
    return img

capture = cv2.VideoCapture(0)

def get_form_cam():
    global capture
    ret, frame = capture.read()
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("show_time", img)
    img = cv2.resize(img, (640, 480))
    return img


def find_value_faster(img11):
    left_start=0
    right_start=640
    up_start=60
    down_start = 80       # 提取需要处理的部分图像
    img_part = img11[up_start:down_start, left_start:right_start]         # 将图像转换为布尔类型的数组，表示像素值是否大于等于128
    bool_img = img_part >= 128         # 沿水平方向对布尔数组进行求和，得到每列像素值大于等于128的数量
    finally_list = np.sum(bool_img, axis=0)
    pressed_pix = 2  # 请替换为合适的值
    # 计算中间数值
    mid_num = int((right_start + left_start) / 2)
    i = 320
    while finally_list[i] <= pressed_pix and 1<i<639:
        i = i + 1
    right_line = i
    i =320
    while finally_list[i] <= pressed_pix and 1<i<639:
        i = i - 1
    left_line = i         # 查找右边界
    pressed_pix = 10  # 请替换为合适的值
    line = (left_line + right_line) / 2
    return line, left_line, right_line



def show_img(img):
    try:
        cv2.imshow("show_time", img)
        cv2.waitKey(0)
    except FileNotFoundError:
        return False
    return True


def find_line():
    raw = get_from_file()
    start_location_x = 0
    start_location_y = 240
    end_location_x = 640
    end_location_y = 480
    # 在意的图像范围，即线条出现的图像范围


    in_doing = raw[start_location_y:end_location_y, start_location_x:end_location_x]
    # cv2.cvtColor(in_doing, cv2.COLOR_BGR2GRAY)
    in_doing = cv2.GaussianBlur(in_doing, (25,25), sigmaX=0, sigmaY=0)


    edge_get = cv2.adaptiveThreshold(in_doing, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 81, -7)
    #edge_get = cv2.Sobel(src=in_doing, ddepth=cv2.CV_64F, dx=2, dy=1, ksize=11)  # Combined X and Y Sobel Edge Detection
    #kernel = np.ones((3, 7), dtype=np.uint8)
    #edge_get = cv2.erode(edge_get,kernel,1)
    kernel = np.ones((3, 3), dtype=np.uint8)
    edge_get = cv2.erode(edge_get, kernel, 3)

    show_img(edge_get)
    # ret, in_doing = cv2.threshold(in_doing, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    line, left_line, right_line = find_value_faster(edge_get)
    draw_0 = cv2.rectangle(in_doing, (left_line, 60), (right_line, 80), (255, 0, 0), 2)
    show_img(draw_0)
    if right_line == 639:
        flag = "right"
    elif  left_line == 0:
        flag = "left"
    else:
        flag = "nothing"
    return line, flag





if __name__ == "__main__":

        while True:
            find_line()
            time.sleep(1)

