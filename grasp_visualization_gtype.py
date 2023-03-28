from hand_config import *
from object_config import colorlib, objects
from utils import *
import open3d as o3d


if __name__ == "__main__":
    object_cls = objects['mug']
    gtype = 'handle'
    save_path = 'obj_coordinate/pcd_gposes/' + object_cls.name
    gposes_path = save_path + '/' + 'gposes_raw.txt'
    gtypes_path = save_path + '/' + 'gtypes.txt'
    gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)

    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = object_cls.init_transform()
    # Hand
    init_hand = load_mano()

    meshes = [coordinate, object_mesh]
    label = np.loadtxt(save_path + '/' + str(gtype)+'_label.txt')
    for i in range(gtype_poses.shape[0]):
        pose = gtype_poses[i]
        hand_gpose = hand_transform(pose, init_hand)
        hand_gpose.paint_uniform_color(colorlib[int(label[i])])
        meshes.append(hand_gpose)
        # if i >= 2:
        #     break

    # AVG
    # gposes_avg_path = save_path + '/' + 'gposes_label_avg.txt'
    # gposes_label_avg = np.loadtxt(gposes_avg_path)
    # gposes = gposes_label_avg[:, :-1]
    # labels = gposes_label_avg[:, -1]
    # for i, gpose in enumerate(gposes):
    #     hand_gtype = hand_transform(gpose, init_hand)
    #     color_idx = int(labels[i])
    #     hand_gtype.paint_uniform_color(colorlib[color_idx])
    #     meshes.append(hand_gtype)

    field_path = 'obj_coordinate/pcd_field/' + object_cls.name
    pcd = o3d.io.read_point_cloud(field_path + '/' + str(gtype) +'.xyzrgb')
    # pcd = o3d.io.read_point_cloud(field_path + '/' + 'field_position.xyz')
    meshes.append(pcd)
    o3d.visualization.draw_geometries(meshes)