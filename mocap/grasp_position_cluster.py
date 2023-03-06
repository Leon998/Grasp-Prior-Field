"""
Cluster grasp poses, just using xyz
"""
from utils import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Grasp cluster
    path = "./227_partial/jug/"
    q_grasps_oh, t_grasps_oh, tf_grasps_oh = grasp_integrate(path)
    fig, ax, label = position_cluster(t_grasps_oh, num_clusters=4)
    # fig, ax, label = pose_cluster(tf_grasps_oh, num_clusters=4)
    ax.set_title('3d Scatter plot')
    plt.show()


