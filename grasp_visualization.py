from hand_config import *
from utils import *


if __name__ == "__main__":
    gtype = 'handle'
    gposes_path = 'mocap/pcd_gposes/mug_gposes_raw.txt'
    gtypes_path = 'mocap/pcd_gposes/mug_gtypes.txt'
    gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)

    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = mug.init_transform()
    # Hand
    init_hand = load_mano()

    meshes = [coordinate, object_mesh]
    label = np.loadtxt('mocap/pcd_gposes/mug_'+str(gtype)+'_label.txt')
    for i in range(gtype_poses.shape[0]):
        pose = gtype_poses[i]
        hand_gtype = hand_transform(pose, init_hand)
        hand_gtype.paint_uniform_color(colorlib[int(label[i])])
        meshes.append(hand_gtype)

    pcd = o3d.io.read_point_cloud('mocap/pcd_trajs/mug_'+str(gtype)+'_manifolds.xyzrgb')
    meshes.append(pcd)
    o3d.visualization.draw_geometries(meshes)