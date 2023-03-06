import open3d as o3d
import copy
import numpy as np
from hand_config import *
from object_config import *


if __name__ == "__main__":
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = mug.init_transform()

    # Hand
    init_hand = load_mano()
    mug_grasps = np.loadtxt('./mocap/pcd_transforms/mug_301_raw.txt')
    pose0 = mug_grasps[0]
    pose1 = mug_grasps[36]
    pose2 = mug_grasps[109]

    hand_handle = hand_transform(pose0, init_hand)
    hand_handle.paint_uniform_color([142/255, 207/255, 201/255])
    hand_side = hand_transform(pose1, init_hand)
    hand_side.paint_uniform_color([250/255, 127/255, 111/255])
    hand_top = hand_transform(pose2, init_hand)
    hand_top.paint_uniform_color([255/255, 190/255, 122/255])

    # Trajectory
    pcd = o3d.io.read_point_cloud('./mocap/pcd_locations/mug_301_traj_label.xyzrgb')

    o3d.visualization.draw_geometries([coordinate, object_mesh, pcd, hand_handle, hand_side, hand_top])