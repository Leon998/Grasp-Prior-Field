import open3d as o3d
import numpy as np


class Object:
    def __init__(self, file_path, init_pose):
        self.file_path = file_path
        self.init_pose = init_pose
        # self.color_label = color_label

    def init_transform(self):
        object_mesh = o3d.io.read_triangle_mesh(self.file_path, True)
        R = object_mesh.get_rotation_matrix_from_xyz(self.init_pose)
        object_mesh.rotate(R)
        return object_mesh


mug = Object('./ycb_models/025_mug/textured.obj', (-np.pi / 2, 0, 0))


