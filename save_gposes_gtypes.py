"""
Saving grasp points poses and grasp types
"""
from utils import *
import numpy as np
from object_config import mug, cracker_box

if __name__ == "__main__":
    object_cls = cracker_box
    path = 'mocap/' + object_cls.name + '/'
    q_grasps_oh, t_grasps_oh, tf_grasps_oh, grasp_type_names = grasp_integrate(path, object_cls.grasp_types)
    # Saving pose information
    np.savetxt('mocap/pcd_gposes/' + object_cls.name + '_gposes_raw.txt', tf_grasps_oh)
    # Saving grasp type index
    with open('mocap/pcd_gposes/' + object_cls.name + '_gtypes.txt', 'w') as f:
        for idx in grasp_type_names:
            f.write(idx + '\n')


