from hand_config import *
from object_config import colorlib, objects
from utils import *


if __name__ == "__main__":
    object_cls = objects['bowl']
    gtype = 's1'
    save_path = 'mocap/pcd_gposes/' + object_cls.name
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
        hand_gtype = hand_transform(pose, init_hand)
        hand_gtype.paint_uniform_color(colorlib[int(label[i])])
        meshes.append(hand_gtype)
        # if i >= 2:
        #     break

    save_path_traj = 'mocap/pcd_trajs/' + object_cls.name
    pcd = o3d.io.read_point_cloud(save_path_traj + '/' + str(gtype) +'_manifolds.xyzrgb')
    meshes.append(pcd)
    o3d.visualization.draw_geometries(meshes)