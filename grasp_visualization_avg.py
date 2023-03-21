import numpy as np

from hand_config import *
from object_config import colorlib, objects
from utils import *
import open3d as o3d


if __name__ == "__main__":
    object_cls = objects['mug']
    save_path = 'obj_coordinate/pcd_gposes/' + object_cls.name
    gposes_avg_path = save_path + '/' + 'gposes_label_avg.txt'
    field_path = 'obj_coordinate/pcd_field/' + object_cls.name

    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = object_cls.init_transform()
    # Hand
    init_hand = load_mano()
    meshes = [coordinate, object_mesh]

    gposes_label_avg = np.loadtxt(gposes_avg_path)
    gposes = gposes_label_avg[:, :-1]
    labels = gposes_label_avg[:, -1:]
    for i, gpose in enumerate(gposes):
        hand_gtype = hand_transform(gpose, init_hand)
        color_idx = int(labels[i][0])
        hand_gtype.paint_uniform_color(colorlib[color_idx])
        meshes.append(hand_gtype)

    pcd = o3d.io.read_point_cloud(field_path + '/' + 'T_colored.xyzrgb')
    meshes.append(pcd)
    o3d.visualization.draw_geometries(meshes)