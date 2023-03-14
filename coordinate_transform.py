"""
Transform world coordinate into object coordinate, and save as txt file.
The transforms include the whole motion (trajectory and grasp pose)
"""
import os
from utils import *
import numpy as np
from object_config import objects


if __name__ == "__main__":
    object_cls = objects['bowl']
    path = 'mocap/' + object_cls.name + '/'
    # Saving path
    save_path = 'obj_coordinate/' + object_cls.name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # Source files
    source_files = os.listdir(path)
    source_files.sort()
    for i, file in enumerate(source_files):
        file_path = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_path)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
        np.savetxt(save_path + '/' + file[:-3] + 'txt', TF_oh)

    # hand_poses = np.loadtxt('obj_coordinate/mug/handle_000.txt')
    # print(hand_poses.shape[0])
    # q_oh = hand_poses[-1, :4]
    # t_oh = hand_poses[-1, 4:]
    # tf_oh = hand_poses[-1, :]
    # print(q_oh, t_oh, tf_oh)
