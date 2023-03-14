"""
save a field containing gtype and cluster labels
"""
import numpy as np
from utils import *
from object_config import colorlib, objects
import os


def label_stack(label, num_frame):
    labels = np.zeros((1, 2))
    for i in range(num_frame):
        labels = np.concatenate((labels, label), axis=0)
    labels = labels[1:, :]
    return labels


if __name__ == "__main__":
    object_cls = objects['mug']
    Traj_T_oh = np.zeros((1, 5))
    for j, gtype in enumerate(object_cls.grasp_types):
        # j is the grasp type index
        save_path = 'mocap/pcd_gposes/' + object_cls.name
        if not os.path.exists(save_path):
            os.mkdir(save_path)
        gposes_path = save_path + '/' + 'gposes_raw.txt'
        gtypes_path = save_path + '/' + 'gtypes.txt'
        gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)
        print(gtype_indices)

        # Clustering and saving labels.
        # fig, ax, label = pose_cluster(gtype_poses, num_clusters=4)
        fig, ax, label = position_cluster(gtype_poses[:, 4:], num_clusters=4)
        print(label)
        np.savetxt(save_path + '/' + str(gtype) + '_label.txt', label, fmt="%i")

        # Saving trajectories
        path = 'mocap/' + object_cls.name + '/'
        files = os.listdir(path)
        files.sort()  # Sort all the files in order
        gtype_files = []
        for idx in gtype_indices:
            gtype_files.append(files[idx])

        for i, file in enumerate(gtype_files):
            file_name = path + file
            Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_name)
            Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
            labels = label_stack(np.array([j, label[i]]).reshape(1, 2), num_frame)
            tmp = np.concatenate((T_oh, labels), axis=1)
            Traj_T_oh = np.concatenate((Traj_T_oh, tmp), axis=0)
    # End of all trajectory points, all of them are stacked together
    Traj_T_oh = Traj_T_oh[1:, :]
    # print(Traj_T_oh)
    # print(Traj_T_oh.shape)
    save_path_field = 'mocap/pcd_field/' + object_cls.name
    if not os.path.exists(save_path_field):
        os.mkdir(save_path_field)
    np.savetxt(save_path_field + '/' + 'field.txt', Traj_T_oh)  # Here lost the first 2 components
    np.savetxt(save_path_field + '/' + 'field.xyz', Traj_T_oh[:, :3])
