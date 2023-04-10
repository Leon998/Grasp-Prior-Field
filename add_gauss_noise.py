import os
from utils import *
import numpy as np
from object_config import objects
from hand_config import *
import open3d as o3d


def add_gaussian_noise(input, mean=0, std=0.2):
    noise = np.random.normal(mean, std, input.shape)
    noisy_input = input + noise
    return noisy_input


def add_pose_noise(cutted_TF_oh, std_q=0.08, std_t=0.008):
    tmp = np.zeros((1, 7))
    for hand_pose in cutted_TF_oh[:-1]:
        for _ in range(3):
            noisy_q = add_gaussian_noise(hand_pose[:4], 0, std_q)
            noisy_t = add_gaussian_noise(hand_pose[4:], 0, std_t)
            noisy_hand_pose = np.concatenate((noisy_q, noisy_t))
            tmp = np.concatenate((tmp, noisy_hand_pose.reshape(1, 7)), axis=0)
    tmp = tmp[1:]
    noisy_TF_oh = np.concatenate((tmp, cutted_TF_oh), axis=0)
    return noisy_TF_oh



if __name__ == "__main__":
    object_cls = objects['mug']
    path = 'mocap/' + object_cls.name + '/'
    # Source files
    source_files = os.listdir(path)
    source_files.sort()
    files = source_files[0:5]

    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = object_cls.init_transform()
    # Hand
    init_hand = load_mano()
    meshes = [coordinate, object_mesh]

    for j, file in enumerate(files):
        file_path = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_path)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
        # If cutting is needed
        length = TF_oh.shape[0]
        cutted_start = int(0.2 * length)
        cutted_end = int(0.7 * length)
        gpose = TF_oh[-1, :].reshape(1, 7)
        cutted_TF_oh = np.concatenate((TF_oh[cutted_start:cutted_end, :], gpose), axis=0)