import open3d as o3d
import copy
import numpy as np
from hand_config import *
from object_config import *
from mocap.utils import *


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

    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = mug.init_transform()
    # Hand
    init_hand = load_mano()

    meshes = [coordinate, object_mesh]
    label = np.loadtxt('mocap/pcd_gposes/mug_'+str(gtype)+'_manifold.txt')
    print(label)
    for i in range(gtype_poses.shape[0]):
        pose = gtype_poses[i]
        hand_gtype = hand_transform(pose, init_hand)
        hand_gtype.paint_uniform_color(colorlib[int(label[i])])
        meshes.append(hand_gtype)

    pcd = o3d.io.read_point_cloud('mocap/pcd_trajs/mug_'+str(gtype)+'_clustered.xyzrgb')
    meshes.append(pcd)
    o3d.visualization.draw_geometries(meshes)