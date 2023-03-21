from hand_config import *
from object_config import colorlib, objects
from utils import *
import open3d as o3d
import numpy as np


def save_gpose_avg(object_cls):
    gtypes = object_cls.grasp_types
    save_path = 'obj_coordinate/pcd_gposes/' + object_cls.name
    gposes_path = save_path + '/' + 'gposes_raw.txt'
    gpose_label_path = save_path + '/' + 'gposes_label.txt'
    gposes = np.loadtxt(gposes_path)
    gpose_label = np.loadtxt(gpose_label_path)
    label = []  # 4-number system transform
    for l in gpose_label:
        tmp = int(l[0] * 4 + l[1])
        label.append(tmp)
    item = np.unique(np.array(label))  # unique gtype number
    index_list = np.arange(len(label))  # index list
    g_pose_avg = []
    for i, g in enumerate(item):
        g_index = index_list[label == g]
        g_gposes = gposes[g_index]
        g_avg = np.mean(g_gposes, axis=0)
        g_pose_avg.append(g_avg)
    gposes_avg = np.array(g_pose_avg)
    # print(gposes_label_avg.shape)
    cls_idx = np.array(item).reshape(len(item), 1)
    # print(cls_idx)
    gposes_avg = np.concatenate((gposes_avg, cls_idx), axis=1)
    np.savetxt(save_path + '/' + 'gposes_label_avg.txt', gposes_avg)


if __name__ == "__main__":
    object_cls = objects['mug']
    save_gpose_avg(object_cls)