import open3d as o3d
import numpy as np


class Object:
    def __init__(self, file_path, init_pose, grasp_types):
        self.file_path = file_path
        self.init_pose = init_pose
        self.grasp_types = grasp_types
        # self.color_label = color_label

    def init_transform(self):
        object_mesh = o3d.io.read_triangle_mesh(self.file_path, True)
        R = object_mesh.get_rotation_matrix_from_xyz(self.init_pose)
        object_mesh.rotate(R)
        return object_mesh


color0 = [142/255, 207/255, 201/255]
color1 = [255/255, 190/255, 122/255]
color2 = [250/255, 127/255, 111/255]
color3 = [130/255, 176/255, 210/255]
color4 = [190/255, 184/255, 220/255]
color5 = [147/255, 75/255, 67/255]
color6 = [177/255, 206/255, 70/255]
color7 = [99/255, 227/255, 152/255]
color8 = [246/255, 202/255, 229/255]
colors = [color0, color1, color2, color3, color4, color5, color6, color7, color8]

mug_model_path = './ycb_models/025_mug/textured.obj'
mug_grasp_types = ['handle', 'side', 'top']
mug = Object(mug_model_path, (-np.pi / 2, 0, 0), mug_grasp_types)

# bowl_model_path = './ycb_models/024_bowl/textured.obj'
# bowl_grasp_types


if __name__ == "__main__":
    print(mug.grasp_types)