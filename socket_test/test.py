import numpy as np
import math
def quaternion_to_euler(w, z):
    # 计算旋转角度（角度）
    theta = 2 * np.arccos(w)
    theta_deg = np.degrees(theta).astype(int)
    euler_angle_z = theta_deg * np.sign(z)
    if euler_angle_z <= 0:
        euler_angle_z + 360
    euler_angle_z = (euler_angle_z * math.pi)/180
    return euler_angle_z

def ola_quaternion_trans(theta):
    """

    :param theta (0, 2pi)
    :return: list
    """
    if theta > math.pi:
        theta -= 2 * math.pi
    # 将角度转换为弧度
    theta_rad = theta * np.pi / 180
    # 计算 cos(theta/2) 和 sin(theta/2)
    cos_theta_half = np.cos(theta_rad / 2)
    sin_theta_half = np.sin(theta_rad / 2)
    # 构建四元数并保留三位有效数字
    quaternion = [0, 0, round(sin_theta_half, 3), round(cos_theta_half, 3)]
    # X,Y z w
    return quaternion
# 测试函数
w = 0.7071  # 示例四元数的 w 分量
z = -0.7071  # 示例四元数的 z 分量

euler_angle_z = ola_quaternion_trans(330)
print("欧拉角绕 Z 轴的旋转：", euler_angle_z)