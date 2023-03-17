import open3d as o3d
import numpy as np


class Object:
    def __init__(self,
                 name,
                 file_path,
                 init_pose,
                 grasp_types,
                 rotate_expansion=False):
        self.name = name
        self.file_path = file_path
        self.init_pose = init_pose
        self.grasp_types = grasp_types
        self.rotate_expansion = rotate_expansion
        # self.color_label = color_label

    def init_transform(self):
        object_mesh = o3d.io.read_triangle_mesh(self.file_path, True)
        R = object_mesh.get_rotation_matrix_from_xyz(self.init_pose)
        object_mesh.rotate(R)
        return object_mesh


color0 = [142 / 255, 207 / 255, 201 / 255]
color1 = [255 / 255, 190 / 255, 122 / 255]
color2 = [250 / 255, 127 / 255, 111 / 255]
color3 = [130 / 255, 176 / 255, 210 / 255]
color4 = [190 / 255, 184 / 255, 220 / 255]
color5 = [147 / 255, 75 / 255, 67 / 255]
color6 = [177 / 255, 206 / 255, 70 / 255]
color7 = [99 / 255, 227 / 255, 152 / 255]
color8 = [246 / 255, 202 / 255, 229 / 255]
colorlib = [color0, color1, color2, color3, color4, color5, color6, color7, color8]

objects = {}

master_chef_can = Object(name='master_chef_can',
                         file_path='./ycb_models/002_master_chef_can/textured.obj',
                         init_pose=(-np.pi / 2, 0, -np.pi / 3),
                         grasp_types=['side', 'top'])
objects['master_chef_can'] = master_chef_can

cracker_box = Object(name='cracker_box',
                     file_path='./ycb_models/003_cracker_box/textured.obj',
                     init_pose=(-np.pi / 2, 0, 0),
                     grasp_types=['side', 'top'],
                     rotate_expansion=True)
objects['cracker_box'] = cracker_box

sugar_box = Object(name='sugar_box',
                   file_path='./ycb_models/004_sugar_box/textured.obj',
                   init_pose=(-np.pi / 2, 0, 0),
                   grasp_types=['side', 'top', 'wide'],
                   rotate_expansion=True)
objects['sugar_box'] = sugar_box

tomato_soup_can = Object(name='tomato_soup_can',
                         file_path='./ycb_models/005_tomato_soup_can/textured.obj',
                         init_pose=(-np.pi / 2, 0, -np.pi / 2),
                         grasp_types=['side', 'top'],
                         rotate_expansion=True)
objects['tomato_soup_can'] = tomato_soup_can

mustard_bottle = Object(name='mustard_bottle',
                        file_path='./ycb_models/006_mustard_bottle/textured.obj',
                        init_pose=(-np.pi / 2, 0, -np.pi / 3),
                        grasp_types=['side1', 'side2', 'top'],
                        rotate_expansion=True)
objects['mustard_bottle'] = mustard_bottle

tuna_fish_can = Object(name='tuna_fish_can',
                       file_path='./ycb_models/007_tuna_fish_can/textured.obj',
                       init_pose=(-np.pi / 2, 0, -np.pi * 4 / 9),
                       grasp_types=['side', 'top'])
objects['tuna_fish_can'] = tuna_fish_can

pudding_box = Object(name='pudding_box',
                     file_path='./ycb_models/008_pudding_box/textured.obj',
                     init_pose=(0, np.pi / 2, -np.pi * 1.05 / 7),
                     grasp_types=['side', 'top', 'wide'],
                     rotate_expansion=True)
objects['pudding_box'] = pudding_box

gelatin_box = Object(name='gelatin_box',
                     file_path='./ycb_models/009_gelatin_box/textured.obj',
                     init_pose=(0, np.pi / 2, -np.pi * 0.58),
                     grasp_types=['side', 'top', 'wide'],
                     rotate_expansion=True)
objects['gelatin_box'] = gelatin_box

potted_meat_can = Object(name='potted_meat_can',
                         file_path='./ycb_models/010_potted_meat_can/textured.obj',
                         init_pose=(-np.pi / 2, 0, -np.pi / 2),
                         grasp_types=['side', 'top', 'wide'])
objects['potted_meat_can'] = potted_meat_can

banana = Object(name='banana',
                file_path='./ycb_models/011_banana/textured.obj',
                init_pose=(-np.pi / 2, 0, np.pi * 0.1),
                grasp_types=['side'])
objects['banana'] = banana

pitcher_base = Object(name='pitcher_base',
                      file_path='./ycb_models/019_pitcher_base/textured.obj',
                      init_pose=(-np.pi / 2, 0, -np.pi / 4),
                      grasp_types=['handle', 'side', 'top'])
objects['pitcher_base'] = pitcher_base

bleach_cleanser = Object(name='bleach_cleanser',
                         file_path='./ycb_models/021_bleach_cleanser/textured.obj',
                         init_pose=(-np.pi / 2, 0, np.pi / 2),
                         grasp_types=['handle', 'side', 'top'],
                         rotate_expansion=True)
objects['bleach_cleanser'] = bleach_cleanser

bowl = Object(name='bowl',
              file_path='./ycb_models/024_bowl/textured.obj',
              init_pose=(-np.pi / 2, 0, 0),
              grasp_types=['side', 'far', 'near'],
              rotate_expansion=True)
objects['bowl'] = bowl

mug = Object(name='mug',
             file_path='./ycb_models/025_mug/textured.obj',
             init_pose=(-np.pi / 2, 0, 0),
             grasp_types=['handle', 'side', 'top'])
objects['mug'] = mug

power_drill = Object(name='power_drill',
                     file_path='./ycb_models/035_power_drill/textured.obj',
                     init_pose=(0, 0, 0),
                     grasp_types=['handle', 'head'])
objects['power_drill'] = power_drill

wood_block = Object(name='wood_block',
                    file_path='./ycb_models/036_wood_block/textured.obj',
                    init_pose=(-np.pi / 2, 0, np.pi / 13),
                    grasp_types=['side', 'top'],
                    rotate_expansion=True)
objects['wood_block'] = wood_block

scissors = Object(name='scissors',
                  file_path='./ycb_models/037_scissors/textured.obj',
                  init_pose=(-np.pi / 2, 0, np.pi * 0.57),
                  grasp_types=['handle', 'middle', 'head'])
objects['scissors'] = scissors

large_marker = Object(name='large_marker',
                      file_path='./ycb_models/040_large_marker/textured.obj',
                      init_pose=(-np.pi / 2, 0, -np.pi / 2),
                      grasp_types=['handle', 'middle', 'head'])
objects['large_marker'] = large_marker

large_clamp = Object(name='large_clamp',
                     file_path='./ycb_models/051_large_clamp/textured.obj',
                     init_pose=(-np.pi / 2, 0, -np.pi * 0.53),
                     grasp_types=['handle', 'middle', 'head'])
objects['large_clamp'] = large_clamp

extra_large_clamp = Object(name='extra_large_clamp',
                           file_path='./ycb_models/052_extra_large_clamp/textured.obj',
                           init_pose=(-np.pi / 2, 0, 0),
                           grasp_types=['handle', 'middle', 'head'])
objects['extra_large_clamp'] = extra_large_clamp

foam_brick = Object(name='foam_brick',
                    file_path='./ycb_models/061_foam_brick/textured.obj',
                    init_pose=(0, np.pi / 2, 0),
                    grasp_types=['handle', 'middle', 'head'],
                    rotate_expansion=True)
objects['foam_brick'] = foam_brick

if __name__ == "__main__":
    object_cls = objects['foam_brick']
    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = object_cls.init_transform()
    meshes = [coordinate, object_mesh]
    o3d.visualization.draw_geometries(meshes)
