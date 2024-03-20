import math


def broad_with_cv(car_loc_x, car_loc_y, car_way,
                  broad_x, broad_y, broad_way, pix_loc):
    """
    limit the car_way into (0, 2pi)
    """

    flag = "where"
    det_x = broad_x - car_loc_x
    det_y = broad_y - car_loc_y
    pthy = math.atan2(det_y, det_x)
    if pthy < 0:
        pthy += math.pi*2

    # 求出几个象限的分界点
    # 写复杂了，我是傻逼
    # しかし 这个能用
    if car_way >= math.pi / 2:
        arm_1 = car_way - (math.pi / 2)
    else:
        arm_1 = car_way + (3 * math.pi / 2)

    arm_2 = car_way

    if car_way > (3 / 2) * math.pi:
        arm_3 = car_way - (3 / 2) * math.pi
    else:
        arm_3 = car_way + (1 / 2) * math.pi

    if car_way >= math.pi:
        arm_4 = car_way - math.pi
    else:
        arm_4 = car_way + math.pi

    arm_list = [
        arm_1, arm_2, arm_3, arm_4
    ]

    if abs(pthy - car_way) <= math.pi / 4 or math.pi * (7 / 4) < abs(pthy - car_way) <= math.pi * 2:
        flag = "center"
    else:
        # 史
        if pthy < (math.pi * 3 / 2):
            i = 0
            for arm in arm_list:
                if 0 < arm - pthy < (math.pi * 0.5):
                    if i == 2 or i == 3:
                        flag = "shit"
                    elif i == 0:
                        flag = "right_side"
                    elif i == 2:
                        flag = "left_side"
                i += 1
        if pthy >= (math.pi * 3 / 2):
            i = 0
            for arm in arm_list:
                if 0 < pthy - arm < (math.pi * 0.5):
                    if i == 0 or i == 3:
                        flag = "shit"
                    elif i == 1:
                        flag = "right_side"
                    elif i == 2:
                        flag = "left_side"
                i += 1
    # 视觉的位置与雷达位置结合判断
    pix_loc = pix_loc / 640

    if flag != "shit":
        if 0.45 < pix_loc < 0.55 and flag == "center":
            flag = True
        if 0.45 > pix_loc and flag == "right_side":
            flag = True
        if 0.55 < pix_loc and flag == "right_side":
            flag = True
    else:
        flag = False
    long = 0.3  # 距离板子的长度
    return_way = 0
    # 当这个板子和雷达结合起来了的时候再计算需要的坐标点和相关的角度
    if flag:
        if (1 / 2 * math.pi) < abs(broad_way - pthy) < (math.pi * 3 / 2):

            broad_x += math.cos(broad_way) * long
            broad_y += math.sin(broad_way) * long
            if broad_way >= math.pi:
                broad_way = broad_way - math.pi
            else:
                broad_way = broad_way + math.pi
            print("A")
        else:

            broad_x += math.cos(broad_way) * long
            broad_y += math.sin(broad_way) * long
    final_list = [flag, broad_x, broad_y, broad_way]
    return final_list
