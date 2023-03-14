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


def save_sub_field(pcd, label, gtype, field_path):
    """
    save sub-field according to gtypes
    """
    gtype_pcd = np.zeros((1, 6))
    for i, point in enumerate(pcd):
        gtype_idx = int(label[i, 0])
        if object_cls.grasp_types[gtype_idx] == gtype:
            color = np.array(colorlib[int(label[i, 1])]).reshape(1, 3)
            tmp = np.concatenate((point.reshape(1, 3), color), axis=1)
            gtype_pcd = np.concatenate((gtype_pcd, tmp), axis=0)
    gtype_pcd = gtype_pcd[1:, :]
    np.savetxt(field_path + '/' + gtype + '.xyzrgb', gtype_pcd)


if __name__ == "__main__":
    object_cls = objects['bowl']
    Traj_T_oh = np.zeros((1, 5))
    for j, gtype in enumerate(object_cls.grasp_types):
        # j is the grasp type index
        save_path = 'obj_coordinate/pcd_gposes/' + object_cls.name
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
        path = 'obj_coordinate/' + object_cls.name + '/'
        files = os.listdir(path)
        files.sort()  # Sort all the files in order
        gtype_files = []
        for idx in gtype_indices:
            gtype_files.append(files[idx])
        traj_path = 'obj_coordinate/pcd_trajs_labeled/' + object_cls.name
        if not os.path.exists(traj_path):
            os.mkdir(traj_path)
        for i, file in enumerate(gtype_files):
            file_path = path + file
            hand_poses = np.loadtxt(file_path)
            Q_oh = hand_poses[:, :4]
            T_oh = hand_poses[:, 4:]
            TF_oh = hand_poses[:, :]
            num_frame = hand_poses.shape[0]
            labels = label_stack(np.array([j, label[i]]).reshape(1, 2), num_frame)
            tmp = np.concatenate((T_oh, labels), axis=1)
            TF_oh = np.concatenate((TF_oh, labels), axis=1)
            np.savetxt(traj_path + '/' + file[:-3] + 'txt', TF_oh)
            Traj_T_oh = np.concatenate((Traj_T_oh, tmp), axis=0)
    # End of all trajectory points, all of them are stacked together
    Traj_T_oh = Traj_T_oh[1:, :]
    # print(Traj_T_oh)
    # print(Traj_T_oh.shape)
    field_path = 'obj_coordinate/pcd_field/' + object_cls.name
    if not os.path.exists(field_path):
        os.mkdir(field_path)
    np.savetxt(field_path + '/' + 'field_position.txt', Traj_T_oh)  # Here lost the first 2 components
    np.savetxt(field_path + '/' + 'field_position.xyz', Traj_T_oh[:, :3])

    # Saving sub-field
    pcd = Traj_T_oh[:, :3]
    label = Traj_T_oh[:, -2:]
    print(pcd.shape)
    print(label.shape)
    gtypes = object_cls.grasp_types
    for gtype in gtypes:
        save_sub_field(pcd, label, gtype, field_path)