"""
First clutster grasp poses, just using xyz
Then draw the trajectories according to the grasp labels
"""

from utils import *
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    ## Grasp cluster
    path = "./bottle/301/"
    q_grasps_oh, t_grasps_oh, tf_grasps_oh = grasp_integrate(path)
    fig, ax, label = position_cluster(t_grasps_oh, num_clusters=4)
    # fig, ax, label = pose_cluster(TF_grasp_oh, num_clusters=4)

    ## Trajectory visualize, based on the fig and ax from pose_cluster
    files = os.listdir(path)
    i = 0
    for file in files:
        file_name = path + file
        Q_wh, T_wh, Q_wo, T_wo, num_frame = read_data(file_name)
        Q_oh, T_oh, TF_oh = sequence_coordinate_transform(Q_wh, T_wh, Q_wo, T_wo, num_frame)
        # 3D drawing
        l = label[i]
        ax.scatter3D(T_oh[:, 0], T_oh[:, 1], T_oh[:, 2], color=plt.cm.jet(float(l) / np.max(label + 1)))
        # print(T_oh.shape)
        i += 1
        # if i >= 40:
        #     break

    ax.set_title('3d Scatter plot')
    plt.show()
