"""
Saving grasp points poses and grasp types
"""
import os
from utils import *
import numpy as np
from object_config import objects

if __name__ == "__main__":
    object_cls = objects['mug']
    # path = 'mocap/' + object_cls.name + '/'
    # q_grasps_oh, t_grasps_oh, tf_grasps_oh, grasp_type_names = grasp_integrate(path, object_cls.grasp_types)
    # save_path = 'mocap/pcd_gposes/' + object_cls.name
    path = 'obj_coordinate/' + object_cls.name + '/'
    q_grasps_oh, t_grasps_oh, tf_grasps_oh, grasp_type_names = grasp_integrate_new(path, object_cls.grasp_types)
    # Saving pose information
    save_path = 'obj_coordinate/pcd_gposes/' + object_cls.name
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    np.savetxt(save_path + '/' + 'gposes_raw.txt', tf_grasps_oh)
    # Saving grasp type index
    with open(save_path + '/' + 'gtypes.txt', 'w') as f:
        for idx in grasp_type_names:
            f.write(idx + '\n')


