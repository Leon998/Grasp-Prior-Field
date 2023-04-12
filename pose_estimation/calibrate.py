import os
import numpy as np
from hand_config import *
from object_config import colorlib, objects
from scipy.spatial.transform import Rotation as R
from utils import *
import open3d as o3d


def calibration(mocap_path, tagPose):
    # mocap
    Q_wh, T_wh, Q_wtag, T_wtag, num_frame = read_data(mocap_path)
    Q_tagh, T_tagh, TF_tagh = sequence_coordinate_transform(Q_wh, T_wh, Q_wtag, T_wtag, num_frame)
    q_tagh, t_tagh = Q_tagh[-1], T_tagh[-1]
    r_tagh = R.from_quat(q_tagh).as_matrix()
    # print(q_tagh, t_tagh)
    # calibrate
    pose_ctag = np.loadtxt(tagPose)
    r_ctag = pose_ctag[:, :3]
    t_ctag = pose_ctag[:, 3]
    # print(r_ctag, t_ctag)
    r_ch = r_ctag.dot(r_tagh)
    t_ch = r_ctag.dot(t_tagh) + t_ctag
    # print(r_ch, t_ch)
    return r_tagh, t_tagh, r_ch, t_ch


def hand_coordinate_visualize(r_tagh, t_tagh, init_hand, meshes, paint=False):
    q_tagh = R.from_matrix(r_tagh).as_quat()
    hand_coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.07, origin=[0, 0, 0])
    hand_coordinate.translate(t_tagh, relative=True)
    hand_coordinate.rotate(r_tagh, center=t_tagh)
    meshes.append(hand_coordinate)
    hand_pose = np.concatenate((q_tagh.reshape(1, -1), t_tagh.reshape(1, -1)), axis=1).reshape(-1)
    start_hand = hand_transform(hand_pose, init_hand)
    if paint:
        start_hand.paint_uniform_color([150 / 255, 195 / 255, 125 / 255])
    meshes.append(start_hand)


if __name__ == "__main__":
    # Coordinate
    coordinate = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.1, origin=[0, 0, 0])
    # Hand
    init_hand = load_mano()
    meshes = [coordinate]

    # calibrate
    mocap_path = "./hand_eye_calibrate/412_box/412_box_1.csv"
    tagPose_path = "./hand_eye_calibrate/412_box/updated_tagPose_box_1.txt"
    r_tagh, t_tagh, r_ch, t_ch = calibration(mocap_path, tagPose_path)
    print(r_ch, t_ch)

    # visualize
    # hand coordinate and hand
    hand_coordinate_visualize(r_tagh, t_tagh, init_hand, meshes)

    # camera
    camera_extrinsic_path = "./hand_eye_calibrate/412_box/camExtrinsics_box_1.txt"
    pose_tagc = np.loadtxt(camera_extrinsic_path)
    r_tagc = pose_tagc[:, :3]
    t_tagc = pose_tagc[:, 3]
    # print(r_tagc, t_tagc)
    camera = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.05, origin=[0, 0, 0])
    camera.translate(t_tagc, relative=True)
    camera.rotate(r_tagc, center=t_tagc)
    meshes.append(camera)

    o3d.visualization.draw_geometries(meshes)
