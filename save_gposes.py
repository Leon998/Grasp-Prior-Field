"""
Saving grasp points poses.
"""
from mocap.utils import *
import numpy as np
from object_config import mug, colorlib

if __name__ == "__main__":
    path = "mocap/mug/301/"
    q_grasps_oh, t_grasps_oh, tf_grasps_oh, grasp_type_names = grasp_integrate(path, mug.grasp_types)
    # Saving pose information
    np.savetxt('mocap/pcd_gposes/mug_301_raw.txt', tf_grasps_oh)
    # Saving grasp type index
    with open("mocap/pcd_gposes/mug_301_human_label.txt", 'w') as f:
        for idx in grasp_type_names:
            f.write(idx + '\n')


