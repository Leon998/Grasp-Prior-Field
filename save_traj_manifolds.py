"""
Cluster grasp poses and save the corresponding trajectories
"""
import numpy as np

from utils import *
from object_config import mug, colorlib
from hand_config import *


def color_stack(color, num_frame):
    colors = np.zeros((1, 3))
    for i in range(num_frame):
        colors = np.concatenate((colors, color), axis=0)
    colors = colors[1:, :]
    return colors


if __name__ == "__main__":
    gtype = 'handle'
    gposes_path = 'mocap/pcd_gposes/mug_gposes_raw.txt'
    gtypes_path = 'mocap/pcd_gposes/mug_gtypes.txt'
    gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)

    # Clustering and saving labels
    fig, ax, label = pose_cluster(gtype_poses, num_clusters=4)
    print(label)
    np.savetxt('mocap/pcd_gposes/mug_' + str(gtype) + '_label.txt', label, fmt="%i")

    # Saving trajectories
    path = 'mocap/mug/'
    files = os.listdir(path)
    files.sort()  # Sort all the files in order
    gtype_files = []
    for idx in gtype_indices:
        gtype_files.append(files[idx])

    gtype_Traj_T_oh_rgb = np.zeros((1, 6))
    traj_frames = []
    for i, file in enumerate(gtype_files):
        file_name = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_name)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
        colors = color_stack(np.array(colorlib[int(label[i])]).reshape(1, 3), num_frame)
        tmp = np.concatenate((T_oh, colors), axis=1)
        gtype_Traj_T_oh_rgb = np.concatenate((gtype_Traj_T_oh_rgb, tmp), axis=0)
    gtype_Traj_T_oh_rgb = gtype_Traj_T_oh_rgb[1:, :]
    print(gtype_Traj_T_oh_rgb.shape)
    np.savetxt('mocap/pcd_trajs/mug_' + str(gtype) +'_manifolds.xyzrgb', gtype_Traj_T_oh_rgb)