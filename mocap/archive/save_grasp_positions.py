"""
Saving grasp position points.
"""
from utils import *
import numpy as np


if __name__ == "__main__":
    # path = "./mug/301/"
    # q_grasps_oh, t_grasps_oh, tf_grasps_oh = grasp_integrate(path)
    #
    # np.savetxt('./pcd/mug_301_grasps.xyz', t_grasps_oh)

    ## Grasp with human labels
    color1 = np.array([99 / 255, 227 / 255, 152 / 255]).reshape(1, 3)
    color2 = np.array([147 / 255, 148 / 255, 231 / 255]).reshape(1, 3)
    color3 = np.array([95 / 255, 151 / 255, 210 / 255]).reshape(1, 3)
    path = "../bowl/302/"
    files = os.listdir(path)
    t_grasps_oh = np.zeros((len(files), 6))
    i = 0

    for file in files:
        file_name = path + file
        Q_wh, T_wh, Q_wo, T_wo, _ = read_data(file_name)
        q_oh, t_oh, tf_oh = extract_grasp(Q_wh, T_wh, Q_wo, T_wo)

        if file[:2] == "s1":
            t_grasps_oh[i, 3:] = color1[0, :]
        elif file[:2] == "s2":
            t_grasps_oh[i, 3:] = color2[0, :]
        else:
            t_grasps_oh[i, 3:] = color3[0, :]
        t_grasps_oh[i, :3] = t_oh[:]
        i += 1

    print(t_grasps_oh)
    # t_grasps_oh = t_grasps_oh[1:, :]  # tf_grasps_oh contains translate

    np.savetxt('./pcd_locations/bowl_302_grasp_label.xyzrgb', t_grasps_oh)