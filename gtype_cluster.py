"""
Cluster grasp poses
"""
from utils import *
from object_config import objects, colorlib
from hand_config import *

if __name__ == "__main__":
    object_cls = objects['bowl']
    gtype = 's3'
    save_path = 'mocap/pcd_gposes/' + object_cls.name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    gposes_path = save_path + '/' + 'gposes_raw.txt'
    gtypes_path = save_path + '/' + 'gtypes.txt'
    gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)


    # Clustering and saving labels
    # fig, ax, label = pose_cluster(gtype_poses, num_clusters=4)
    fig, ax, label = position_cluster(gtype_poses[:, 4:], num_clusters=4)
    print(label)

    # Hand visualization test
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    object_mesh = object_cls.init_transform()
    init_hand = load_mano()

    meshes = [coordinate, object_mesh]
    for i in range(gtype_poses.shape[0]):
        pose = gtype_poses[i]
        hand_handle = hand_transform(pose, init_hand)
        hand_handle.paint_uniform_color(colorlib[label[i]])
        meshes.append(hand_handle)
        # if i >= 2:
        #     break

    o3d.visualization.draw_geometries(meshes)




