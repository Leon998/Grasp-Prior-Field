"""
Saving grasp points poses.
"""
from utils import *
import numpy as np


if __name__ == "__main__":
    path = "./mug/301/"
    q_grasps_oh, t_grasps_oh, tf_grasps_oh = grasp_integrate(path)
    print(tf_grasps_oh)
    np.savetxt('./pcd_transforms/mug_301_raw.txt', tf_grasps_oh)