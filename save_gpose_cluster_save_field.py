"""
save a field containing gtype and cluster labels
"""
import numpy as np
from utils import *
from object_config import colorlib, objects
import os
from save_gpose_average import save_gpose_avg


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
    object_cls = objects['power_drill']
    # ====================================== Save gposes gtypes ============================== #
    path = 'obj_coordinate/' + object_cls.name + '/'
    q_grasps_oh, t_grasps_oh, tf_grasps_oh, grasp_type_names = grasp_integrate(path, object_cls.grasp_types)
    # Saving pose information
    save_path = 'obj_coordinate/pcd_gposes/' + object_cls.name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    np.savetxt(save_path + '/' + 'gposes_raw.txt', tf_grasps_oh)
    # Saving grasp type index_list
    with open(save_path + '/' + 'gtypes.txt', 'w') as f:
        for gtype in grasp_type_names:
            f.write(gtype + '\n')
    # ======================================================================================= #
    Traj_TF_oh_labeled = np.zeros((1, 9))
    gposes_labeled = np.zeros((1, 2))
    gposes_path = save_path + '/' + 'gposes_raw.txt'
    gtypes_path = save_path + '/' + 'gtypes.txt'
    for j, gtype in enumerate(object_cls.grasp_types):
        # j is the grasp type index_list
        gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)
        # print(gtype_indices)

        # ========================== Clustering and saving labels ========================== #
        # fig, ax, label = pose_cluster(gtype_poses, num_clusters=4)
        fig, ax, label = position_cluster(gtype_poses[:, 4:], num_clusters=4)
        print('label: ', label)
        np.savetxt(save_path + '/' + str(gtype) + '_label.txt', label, fmt="%i")
        for idx in range(len(label)):
            gtype = np.array(j).reshape(1, 1)
            glabel = np.array(label[idx]).reshape(1, 1)
            tmp = np.concatenate((gtype, glabel), axis=1)
            gposes_labeled = np.concatenate((gposes_labeled, tmp), axis=0)

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
            tmp = np.concatenate((TF_oh, labels), axis=1)
            TF_oh = np.concatenate((TF_oh, labels), axis=1)
            np.savetxt(traj_path + '/' + file[:-3] + 'txt', TF_oh)
            Traj_TF_oh_labeled = np.concatenate((Traj_TF_oh_labeled, tmp), axis=0)

    # End of all trajectory points, all of them are stacked together
    gposes_labeled = gposes_labeled[1:, :]
    # ======================================= Save gpose_label ======================================== #
    np.savetxt(save_path + '/' + 'gposes_label.txt', gposes_labeled, fmt="%i")
    # ====================================== Save gpose_average ======================================= #
    save_gpose_avg(object_cls)
    # ======================================= Save TF_field ======================================== #
    Traj_TF_oh_labeled = Traj_TF_oh_labeled[1:, :]
    # print(Traj_TF_oh_labeled)
    # print(Traj_TF_oh_labeled.shape)
    field_path = 'obj_coordinate/pcd_field/' + object_cls.name
    if not os.path.exists(field_path):
        os.mkdir(field_path)
    np.savetxt(field_path + '/' + 'TF_field.txt', Traj_TF_oh_labeled)
    # ====================================== Save T_colored ====================================== #
    Traj_T_oh_colored = np.zeros((1, 6))
    for point in Traj_TF_oh_labeled:
        position = point[4:7]
        label = point[7:]
        color_idx = int(label[0] * 4 + label[1])  # 4-number system transform
        color = np.array(colorlib[color_idx])
        t_oh_colored = np.concatenate((position.reshape((1,3)), color.reshape((1,3))), axis=1)
        Traj_T_oh_colored = np.concatenate((Traj_T_oh_colored, t_oh_colored), axis=0)
    Traj_T_oh_colored = Traj_T_oh_colored[1:, :]
    np.savetxt(field_path + '/' + 'T_colored.xyzrgb', Traj_T_oh_colored)
    # ====================================== Save sub-field ===================================== #
    pcd = Traj_TF_oh_labeled[:, 4:7]
    label = Traj_TF_oh_labeled[:, 7:]
    print(pcd.shape)
    print(label.shape)
    gtypes = object_cls.grasp_types
    for gtype in gtypes:
        save_sub_field(pcd, label, gtype, field_path)