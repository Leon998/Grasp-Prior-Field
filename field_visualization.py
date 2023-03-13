from hand_config import *
from object_config import colorlib, objects
from utils import *
import open3d as o3d


def save_sub_field(pcd, label, gtype):
    gtype_pcd = np.zeros((1, 6))
    for i, point in enumerate(pcd):
        gtype_idx = int(label[i, 0])
        if object_cls.grasp_types[gtype_idx] == gtype:
            color = np.array(colorlib[int(label[i, 1])]).reshape(1, 3)
            tmp = np.concatenate((point.reshape(1, 3), color), axis=1)
            gtype_pcd = np.concatenate((gtype_pcd, tmp), axis=0)
    gtype_pcd = gtype_pcd[1:, :]
    np.savetxt(field_path + '/' + gtype + '.xyzrgb', gtype_pcd)


if __name__ == "__main__":
    object_cls = objects['cracker_box']
    field_path = 'mocap/pcd_field/' + object_cls.name

    field = np.loadtxt(field_path + '/' + 'field.txt')
    pcd = field[:, :3]
    label = field[:, -2:]
    print(pcd.shape)
    print(label.shape)

    # for i, point in enumerate(pcd):
    #     gtype_idx = int(label[i, 0])
    #     if object_cls.grasp_types[gtype_idx] == 'topShort':
    #         color = np.array(colorlib[int(label[i, 1])]).reshape(1, 3)
    #         tmp = np.concatenate((point.reshape(1, 3), color), axis=1)
    #         gtype_pcd = np.concatenate((gtype_pcd, tmp), axis=0)
    # gtype_pcd = gtype_pcd[1:, :]
    # np.savetxt(field_path + '/' + 'topShort.xyzrgb', gtype_pcd)
    gtypes = object_cls.grasp_types
    for gtype in gtypes:
        save_sub_field(pcd, label, gtype)

    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = object_cls.init_transform()
    # Hand
    meshes = [coordinate, object_mesh]
    pcd_1 = o3d.io.read_point_cloud(field_path + '/' + 'topShort.xyzrgb')
    meshes.append(pcd_1)

    o3d.visualization.draw_geometries(meshes)
