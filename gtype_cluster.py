"""
Cluster grasp poses
"""
from utils import *
from object_config import mug, colorlib
from hand_config import *

if __name__ == "__main__":
    gtype = 'top'
    gposes_path = 'mocap/pcd_gposes/mug_gposes_raw.txt'
    gtypes_path = 'mocap/pcd_gposes/mug_gtypes.txt'
    gtype_indices, gtype_poses = gtype_extract(gtype, gposes_path, gtypes_path)


    # Clustering and saving labels
    fig, ax, label = pose_cluster(gtype_poses, num_clusters=4)
    print(label)
    np.savetxt('mocap/pcd_gposes/mug_' + str(gtype) + '_label.txt', label, fmt="%i")

    # Hand visualization test
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    object_mesh = mug.init_transform()
    init_hand = load_mano()

    meshes = [coordinate, object_mesh]
    for i in range(gtype_poses.shape[0]):
        pose = gtype_poses[i]
        hand_handle = hand_transform(pose, init_hand)
        hand_handle.paint_uniform_color(colorlib[label[i]])
        meshes.append(hand_handle)

    o3d.visualization.draw_geometries(meshes)




