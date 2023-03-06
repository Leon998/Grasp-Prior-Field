"""
Saving grasp position points.
"""
from utils import *
import numpy as np


def color_stack(color, num_frame):
    colors = np.zeros((1, 3))
    for i in range(num_frame):
        colors = np.concatenate((colors, color), axis=0)
    colors = colors[1:, :]
    return colors


if __name__ == "__main__":
    path = "./bowl/302/"

    # Trajectory visualize, based on the fig and ax from pose_cluster
    files = os.listdir(path)
    all_TrajT_oh = np.zeros((1, 3))
    # Coloring
    rgb_all_TrajT_oh = np.zeros((1, 6))  # color the trajectory if is human-labeled
    color1 = np.array([99 / 255, 227 / 255, 152 / 255]).reshape(1, 3)
    color2 = np.array([147/255, 148/255, 231/255]).reshape(1, 3)
    color3 = np.array([95/255, 151/255, 210/255]).reshape(1, 3)

    for file in files:
        file_name = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_name)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo,
                                                          num_frame)  # T_oh is trajectory position
        if file[:2] == "s1":
            colors = color_stack(color1, num_frame)
        elif file[:2] == "s2":
            colors = color_stack(color2, num_frame)
        else:
            colors = color_stack(color3, num_frame)
        tmp = np.concatenate((T_oh, colors), axis=1)
        rgb_all_TrajT_oh = np.concatenate((rgb_all_TrajT_oh, tmp), axis=0)

        all_TrajT_oh = np.concatenate((all_TrajT_oh, T_oh), axis=0)

    all_TrajT_oh = all_TrajT_oh[1:, :]
    rgb_all_TrajT_oh = rgb_all_TrajT_oh[1:, :]


    print(all_TrajT_oh.shape)
    print(rgb_all_TrajT_oh.shape)

    np.savetxt('./pcd_locations/bowl_302.xyz', all_TrajT_oh)
    np.savetxt('./pcd_locations/bowl_302_traj_label.xyzrgb', rgb_all_TrajT_oh)