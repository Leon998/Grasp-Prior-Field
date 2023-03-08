"""
Cluster grasp poses
"""
from mocap.utils import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from object_config import mug, colorlib
from hand_config import *


def color_stack(color, num_frame):
    colors = np.zeros((1, 3))
    for i in range(num_frame):
        colors = np.concatenate((colors, color), axis=0)
    colors = colors[1:, :]
    return colors


if __name__ == "__main__":
    grasp_types = mug.grasp_types
    print(grasp_types)
    # Reading pose
    grasp_poses = np.loadtxt('mocap/pcd_gposes/mug_301_raw.txt')
    # Reading grasp type name
    human_label_path = 'mocap/pcd_gposes/mug_301_human_label.txt'
    grasp_type_lib = grasp_type_index(human_label_path)

    # Extract grasp types
    gtype = 'top'
    gtype_indices = grasp_type_lib[gtype]
    gtype_poses = grasp_poses[gtype_indices]

    # Clustering
    fig, ax, label = pose_cluster(gtype_poses, num_clusters=4)
    print(label)
    np.savetxt('mocap/pcd_gposes/mug_'+str(gtype)+'_manifold.txt', label, fmt="%i")

    # Hand visualization test
    # coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # object_mesh = mug.init_transform()
    # init_hand = load_mano()
    #
    # meshes = [coordinate, object_mesh]
    # for i in range(gtype_poses.shape[0]):
    #     pose = gtype_poses[i]
    #     hand_gtype = hand_transform(pose, init_hand)
    #     hand_gtype.paint_uniform_color(colorlib[label[i]])
    #     meshes.append(hand_gtype)
    #
    # o3d.visualization.draw_geometries(meshes)

    # Saving trajectories
    path = 'mocap/mug/301/'
    files = os.listdir(path)
    files.sort()  # Sort all the files in order
    gtype_files = []
    for idx in gtype_indices:
        gtype_files.append(files[idx])

    gtype_Traj_T_oh = np.zeros((1, 6))
    for i, file in enumerate(gtype_files):
        file_name = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_name)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
        colors = color_stack(np.array(colorlib[label[i]]).reshape(1, 3), num_frame)
        tmp = np.concatenate((T_oh, colors), axis=1)
        gtype_Traj_T_oh = np.concatenate((gtype_Traj_T_oh, tmp), axis=0)
    gtype_Traj_T_oh = gtype_Traj_T_oh[1:, :]
    print(gtype_Traj_T_oh.shape)
    np.savetxt('mocap/pcd_trajs/mug_'+str(gtype)+'_clustered.xyzrgb', gtype_Traj_T_oh)
