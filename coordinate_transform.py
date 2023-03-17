"""
Transform world coordinate into object coordinate, and save as txt file.
The transforms include the whole motion (trajectory and grasp pose)
"""
import os
from utils import *
import numpy as np
from object_config import objects
import shutil


if __name__ == "__main__":
    object_cls = objects['tomato_soup_can']
    path = 'mocap/' + object_cls.name + '/'
    # Saving path
    save_path = 'obj_coordinate/' + object_cls.name + '/'
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    else:
        shutil.rmtree(save_path)
        os.mkdir(save_path)
    # Source files
    source_files = os.listdir(path)
    source_files.sort()
    for i, file in enumerate(source_files):
        file_path = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_path)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
        np.savetxt(save_path + file[:-3] + 'txt', TF_oh)

    # Rotate Expansion
    if object_cls.rotate_expansion:
        files = os.listdir(save_path)
        files.sort()
        gtype_log = {}
        for file in files:
            gtype = file[:-8]
            gtype_log[gtype] = file[-7:-4]
        print(gtype_log)
        for i, file in enumerate(files):
            gtype = file[:-8]
            index = int(file[-7:-4])  # current index
            file_path = save_path + file
            origin_pose = np.loadtxt(file_path)
            # # ================================ Trajectory test =============================== #
            Q_oh = origin_pose[:, :4]
            T_oh = origin_pose[:, 4:]
            TF_oh = origin_pose[:, :]
            num_frame = origin_pose.shape[0]
            new_Q_oh, new_T_oh, new_TF_oh = sequence_rotate_expansion(Q_oh, T_oh, TF_oh, num_frame)
            new_index = int(gtype_log[gtype]) + index + 1
            if new_index <= 9:
                zeros = '00'
            elif new_index <= 99:
                zeros = '0'
            else:
                zeros = ''
            print(str(gtype) + '_' + zeros + str(new_index) + '.txt')
            np.savetxt(save_path + str(gtype) + '_' +zeros + str(new_index) + '.txt', new_TF_oh)