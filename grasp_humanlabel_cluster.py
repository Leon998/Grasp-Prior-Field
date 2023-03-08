"""
Cluster grasp poses
"""
from mocap.utils import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from object_config import mug, colors
from hand_config import *

if __name__ == "__main__":
    grasp_types = mug.grasp_types
    print(grasp_types)
    # Reading pose
    grasp_poses = np.loadtxt('mocap/pcd_transforms/mug_301_raw.txt')
    # Reading grasp type name
    human_label_path = 'mocap/pcd_transforms/mug_301_human_label.txt'
    grasp_type_lib = grasp_type_index(human_label_path)

    # Extract grasp types
    type_indices = grasp_type_lib['side']
    side_poses = grasp_poses[type_indices]
    print(side_poses.shape)

    fig, ax, label = pose_cluster(side_poses, num_clusters=4)
    print(label)

    # Hand visualization test
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    object_mesh = mug.init_transform()
    init_hand = load_mano()

    meshes = [coordinate, object_mesh]
    for i in range(side_poses.shape[0]):
        pose = side_poses[i]
        hand_handle = hand_transform(pose, init_hand)
        hand_handle.paint_uniform_color(colors[label[i]])
        meshes.append(hand_handle)

    o3d.visualization.draw_geometries(meshes)




