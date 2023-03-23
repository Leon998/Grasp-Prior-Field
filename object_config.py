import open3d as o3d
import numpy as np


class Object:
    def __init__(self,
                 name: object,
                 file_path: object,
                 init_pose: object,
                 grasp_types: object,
                 gtype_clusters,
                 rotate_expansion: object = 0):
        self.name = name
        self.file_path = file_path
        self.init_pose = init_pose
        self.grasp_types = grasp_types
        self.gtype_clusters = gtype_clusters
        self.rotate_expansion = rotate_expansion
        # self.color_label = color_label

    def init_transform(self):
        object_mesh = o3d.io.read_triangle_mesh(self.file_path, True)
        R = object_mesh.get_rotation_matrix_from_xyz(self.init_pose)
        object_mesh.rotate(R)
        return object_mesh


color0 = [154 / 255, 32 / 255, 140 / 255]
color1 = [225 / 255, 18 / 255, 153 / 255]
color2 = [255 / 255, 234 / 255, 234 / 255]
color3 = [245 / 255, 198 / 255, 236 / 255]
color4 = [6 / 255, 40 / 255, 61 / 255]
color5 = [19 / 255, 99 / 255, 223 / 255]
color6 = [71 / 255, 181 / 255, 255 / 255]
color7 = [223/ 255, 246 / 255, 255 / 255]
color8 = [237 / 255, 241 / 255, 214 / 255]
color9 = [157/ 255, 192 / 255, 139 / 255]
color10 = [96 / 255, 153 / 255, 102 / 255]
color11 = [64 / 255, 81 / 255, 59 / 255]
colorlib = [color0, color1, color2, color3, color4, color5, color6,
            color7, color8, color9, color10, color11, color0, color0, color0, color0, color0, color0, color0]

objects = {}
PATH = '/home/shixu/My_env/Grasp-Prior-Field/'

master_chef_can = Object(name='master_chef_can',
                         file_path=PATH+'ycb_models/002_master_chef_can/textured.obj',
                         init_pose=(-np.pi / 2, 0, -np.pi / 3),
                         grasp_types=['side', 'top'],
                         rotate_expansion=90)
objects['master_chef_can'] = master_chef_can

cracker_box = Object(name='cracker_box',
                     file_path=PATH+'ycb_models/003_cracker_box/textured.obj',
                     init_pose=(-np.pi / 2, 0, 0),
                     grasp_types=['side', 'top'],
                     rotate_expansion=180)
objects['cracker_box'] = cracker_box

sugar_box = Object(name='sugar_box',
                   file_path=PATH+'ycb_models/004_sugar_box/textured.obj',
                   init_pose=(-np.pi / 2, 0, 0),
                   grasp_types=['side', 'top', 'wide'],
                   rotate_expansion=180)
objects['sugar_box'] = sugar_box

tomato_soup_can = Object(name='tomato_soup_can',
                         file_path=PATH+'ycb_models/005_tomato_soup_can/textured.obj',
                         init_pose=(-np.pi / 2, 0, -np.pi / 2),
                         grasp_types=['side', 'top'],
                         rotate_expansion=90)
objects['tomato_soup_can'] = tomato_soup_can

mustard_bottle = Object(name='mustard_bottle',
                        file_path=PATH+'ycb_models/006_mustard_bottle/textured.obj',
                        init_pose=(-np.pi / 2, 0, -np.pi / 3),
                        grasp_types=['side1', 'side2', 'top'],
                        rotate_expansion=180)
objects['mustard_bottle'] = mustard_bottle

tuna_fish_can = Object(name='tuna_fish_can',
                       file_path=PATH+'ycb_models/007_tuna_fish_can/textured.obj',
                       init_pose=(-np.pi / 2, 0, -np.pi * 4 / 9),
                       grasp_types=['side', 'top'],
                       rotate_expansion=90)
objects['tuna_fish_can'] = tuna_fish_can

pudding_box = Object(name='pudding_box',
                     file_path=PATH+'ycb_models/008_pudding_box/textured.obj',
                     init_pose=(0, np.pi / 2, -np.pi * 1.05 / 7),
                     grasp_types=['side', 'top', 'wide'],
                     rotate_expansion=180)
objects['pudding_box'] = pudding_box

gelatin_box = Object(name='gelatin_box',
                     file_path=PATH+'ycb_models/009_gelatin_box/textured.obj',
                     init_pose=(0, np.pi / 2, -np.pi * 0.58),
                     grasp_types=['side', 'top', 'wide'],
                     rotate_expansion=180)
objects['gelatin_box'] = gelatin_box

potted_meat_can = Object(name='potted_meat_can',
                         file_path=PATH+'ycb_models/010_potted_meat_can/textured.obj',
                         init_pose=(-np.pi / 2, 0, -np.pi / 2),
                         grasp_types=['side', 'top', 'wide'],
                         rotate_expansion=180)
objects['potted_meat_can'] = potted_meat_can

banana = Object(name='banana',
                file_path=PATH+'ycb_models/011_banana/textured.obj',
                init_pose=(-np.pi / 2, 0, np.pi * 0.1),
                grasp_types=['side'])
objects['banana'] = banana

pitcher_base = Object(name='pitcher_base',
                      file_path=PATH+'ycb_models/019_pitcher_base/textured.obj',
                      init_pose=(-np.pi / 2, 0, -np.pi / 4),
                      grasp_types=['handle', 'side', 'top'])
objects['pitcher_base'] = pitcher_base

bleach_cleanser = Object(name='bleach_cleanser',
                         file_path=PATH+'ycb_models/021_bleach_cleanser/textured.obj',
                         init_pose=(-np.pi / 2, 0, np.pi / 2),
                         grasp_types=['handle', 'side', 'top'],
                         rotate_expansion=180)
objects['bleach_cleanser'] = bleach_cleanser

bowl = Object(name='bowl',
              file_path=PATH+'ycb_models/024_bowl/textured.obj',
              init_pose=(-np.pi / 2, 0, 0),
              grasp_types=['side', 'far', 'near'],
              rotate_expansion=90)
objects['bowl'] = bowl

mug = Object(name='mug',
             file_path=PATH+'ycb_models/025_mug/textured.obj',
             init_pose=(-np.pi / 2, 0, 0),
             grasp_types=['handle', 'side', 'top'])
objects['mug'] = mug

power_drill = Object(name='power_drill',
                     file_path=PATH+'ycb_models/035_power_drill/textured.obj',
                     init_pose=(0, 0, 0),
                     grasp_types=['handle', 'head'],
                     gtype_clusters=[6, 6])
objects['power_drill'] = power_drill

wood_block = Object(name='wood_block',
                    file_path=PATH+'ycb_models/036_wood_block/textured.obj',
                    init_pose=(-np.pi / 2, 0, np.pi / 13),
                    grasp_types=['side', 'top'],
                    rotate_expansion=180)
objects['wood_block'] = wood_block

scissors = Object(name='scissors',
                  file_path=PATH+'ycb_models/037_scissors/textured.obj',
                  init_pose=(-np.pi / 2, 0, np.pi * 0.57),
                  grasp_types=['handle', 'middle', 'head'])
objects['scissors'] = scissors

large_marker = Object(name='large_marker',
                      file_path=PATH+'ycb_models/040_large_marker/textured.obj',
                      init_pose=(-np.pi / 2, 0, -np.pi / 2),
                      grasp_types=['handle', 'middle', 'head'])
objects['large_marker'] = large_marker

large_clamp = Object(name='large_clamp',
                     file_path=PATH+'ycb_models/051_large_clamp/textured.obj',
                     init_pose=(-np.pi / 2, 0, -np.pi * 0.53),
                     grasp_types=['handle', 'middle', 'head'])
objects['large_clamp'] = large_clamp

extra_large_clamp = Object(name='extra_large_clamp',
                           file_path=PATH+'ycb_models/052_extra_large_clamp/textured.obj',
                           init_pose=(-np.pi / 2, 0, 0),
                           grasp_types=['handle', 'middle', 'head'])
objects['extra_large_clamp'] = extra_large_clamp

foam_brick = Object(name='foam_brick',
                    file_path=PATH+'ycb_models/061_foam_brick/textured.obj',
                    init_pose=(0, np.pi / 2, 0),
                    grasp_types=['handle', 'middle', 'head'],
                    rotate_expansion=180)
objects['foam_brick'] = foam_brick

if __name__ == "__main__":
    object_cls = objects['mug']
    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.2, origin=[0, 0, 0])
    # Object
    object_mesh = object_cls.init_transform()
    meshes = [coordinate, object_mesh]
    o3d.visualization.draw_geometries(meshes)
