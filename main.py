#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: hy
"""

import tensorflow as tf
from align_custom import AlignCustom
from mtcnn_detect import MTCNNDetect
from face_feature import FaceFeature
import scipy.misc as sm
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import json
import os
import cv2


class FaceRecGraph(object):
    def __init__(self):
        '''
            There'll be more to come in this class
        '''
        self.graph = tf.Graph();


class FR_Service(object):
    def __init__(self):
        FRGraph = FaceRecGraph()
        # 先FaceFeature再face_detect 因为model里面没有face_detect的权重
        self.feature_extractor = FaceFeature(FRGraph)
        self.face_detector = MTCNNDetect(FRGraph, scale_factor=2) # scale_factor, rescales image for faster detection
        self.face_aligner = AlignCustom()
        self.feature_gallery_filepath = "images/gallery_feats_512D.txt" # 用来存放注册的人脸特征
        # self.register_gallery()

    def register_gallery(self):
        """
        store features for gallery images
        self.feature_gallery_filepath Data Structure:
        {
        "Mike_0": {
            "Center": [XXXD vector],
            "Left": [XXXD vector],
            "Right": [XXXD Vector]
            }
        "Mike_1": {
            ...
            }
        }
        """
        ref_dir = "images/ref"
        features_dict = {}
        files = os.listdir(ref_dir)
        for im_path in files:
            key = im_path.split(".")[0] # name_pos.jpg
            im_path = os.path.join(ref_dir, im_path)
            img = sm.imread(im_path)
            rects, landmarks = self.face_detector.detect_face(img, 80)  # min face size is set to 80x80, rect in rects: (x,y,w,h)
            if len(rects) < 1:
                print("No face is detected")
            elif len(rects) > 1:
                print("More than one face are detected")
            else:
                aligned_face, face_pos = self.face_aligner.align(160, img, landmarks[0])
                aligns = [aligned_face]
                features_arr = self.feature_extractor.get_features(aligns)
                if key not in features_dict.keys():
                    features_dict[key] = {face_pos: features_arr[0].tolist()}
                else:
                    features_dict[key][face_pos] = features_arr[0].tolist()
        with open(self.feature_gallery_filepath, "w") as file:
            file.write(json.dumps(features_dict))
        print("ref features are sotred")


    def findPeople(self, features_arr, positions, thres = 0.6):
        '''
        :param features_arr: a list of 128d Features of all faces on screen
        :param positions: a list of face position types of all faces on screen
        :param thres: distance threshold
        :return: person name and percentage
        '''
        f = open(self.feature_gallery_filepath,'r')
        data_set = json.loads(f.read())
        returnRes = []
        for (i,features_XXXD) in enumerate(features_arr):
            result = "Unknown"
            max_sim = 0
            for person in data_set.keys():
                # print(person + positions[i])
                # person_feature = data_set[person][positions[i]]
                person_feature = data_set[person]['Center'] # only Center pose face for now
                euc_distance = np.sqrt(np.sum(np.square(person_feature - features_XXXD)))
                cos_distance = euc_distance / 2
                cos_similary = 1 - cos_distance # because the features have been normalized, so euc_dis = 2*(1-cos_dis)
                # print(cos_similary)
                # print(np.linalg.norm(person_feature, ord=2))
                # print(np.linalg.norm(features_XXXD, ord=2))
                if cos_similary > max_sim:
                    max_sim = cos_similary
                    result = person.split('_')[0]
            if max_sim <= thres:
                result = "Unknown"
            returnRes.append((result,max_sim))
        return returnRes


def test():
    # === test for one image
    # im_path = "images/IMG_0252.jpg"
    # img = sm.imread(im_path)
    # rects, landmarks = FRS.face_detector.detect_face(img, 80)  # min face size is set to 80x80, rect in rects: (x,y,w,h)
    # aligned_face, face_pos = FRS.face_aligner.align(160, img, landmarks[0])
    # aligns = [aligned_face]
    # positions = [face_pos]
    # features_arr = FRS.feature_extractor.get_features(aligns)
    # # plt.figure(figsize=(9, 6), dpi=90)
    # # plt.imshow(aligned_face)
    # # plt.show()
    # result = FRS.findPeople(features_arr, positions)
    # print(result)


    # === test for real time camara
    vs = cv2.VideoCapture(0) # get input from webcam
    while True:
        _, frame = vs.read()
        # get detected and aligned faces
        rects, landmarks = FRS.face_detector.detect_face(frame, 80)
        aligns = []
        positions = []
        for (i, rect) in enumerate(rects):
            aligned_face, face_pos = FRS.face_aligner.align(160,frame,landmarks[i])
            if len(aligned_face) == 160 and len(aligned_face[0]) == 160:
                aligns.append(aligned_face)
                positions.append(face_pos)
            else:
                print("Align face failed") #log
        # extract features and show recognition result
        if(len(aligns) > 0):
            features_arr = FRS.feature_extractor.get_features(aligns)
            recog_data = FRS.findPeople(features_arr,positions)
            for (i,rect) in enumerate(rects):
                cv2.rectangle(frame,(rect[0],rect[1]),(rect[0] + rect[2],rect[1]+rect[3]),(255,0,0)) #draw bounding box for the face
                str_displayed = recog_data[i][0] + "-" + str(100* round(recog_data[i][1],4) ) + "%" # recog_data[i][0]+" - "+str(recog_data[i][1])+"%"
                cv2.putText(frame,str_displayed,(rect[0],rect[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

def plot_face():
    pami_group = 'images/Group_Photo_2017.jpg'
    tmp = 'images/IMG_0150.JPG'
    frame = sm.imread(tmp)
    rects, landmarks = FRS.face_detector.detect_face(frame, 40)  # min face size is set to 80x80, rect in rects: (x,y,w,h)

    fig,ax = plt.subplots(1)
    ax.imshow(frame)

    # === get aligned faces
    aligns = []
    positions = []
    for (i,rect) in enumerate(rects):
        aligned_face, face_pos = FRS.face_aligner.align(160,frame,landmarks[i])
        if len(aligned_face) == 160 and len(aligned_face[0]) == 160:
            aligns.append(aligned_face)
            positions.append(face_pos)
        else:
            print("Align face failed")  # log

    # === get face features
    if (len(aligns) > 0):
        features_arr = FRS.feature_extractor.get_features(aligns)
        recog_data = FRS.findPeople(features_arr, positions)

    # === plot faces
    for (i,rect) in enumerate(rects):
        # plot face
        face_x = rect[0]
        face_y = rect[1]
        face_width = rect[2]
        face_height = rect[3]
        face_rect = patches.Rectangle((face_x, face_y), face_width, face_height,linewidth=1,edgecolor='r',facecolor='none') #face: frame[face_y:face_y + face_height, face_x:face_x + face_width]
        ax.add_patch(face_rect)
        str_displayed = recog_data[i][0] + "\n" + str(100* round(recog_data[i][1],4) ) + "%"
        plt.text(face_x, face_y + 0.05, str_displayed, ha='center', va='bottom', color='white', fontsize=10)

        # plot landmarks
        c = ['orange', 'deepskyblue', 'chocolate', 'royalblue', '#ffff00',
             '#ff00ff', '#990000', '#999900', '#009900', '#009999']
        shape = []
        for k in range(int(len(landmarks[i]) / 2)): #[x0, x1,..., y0, y1,...]
            shape.append(landmarks[i][k])
            shape.append(landmarks[i][k + 5])
        for idx in range(int(len(shape) / 2)): # [x0,y0, x1,y1, ...], 右眼, 左眼, 鼻子, 右嘴角, 左嘴角
            r = 2
            lx = shape[2 * idx]
            ly = shape[2 * idx + 1]
            l_rect = patches.Rectangle((lx, ly),r*2,r*2, edgecolor=c[idx],facecolor='none')
            ax.add_patch(l_rect)
    plt.show()



if __name__ == '__main__':
    print('Hello world')
    FRS = FR_Service()
    test()
    # plot_face()



    # 然后利用cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # 画出矩行
    # 参数解释
    # 第一个参数：img是原图
    # 第二个参数：（x，y）是矩阵的左上点坐标
    # 第三个参数：（x + w，y + h）是矩阵的右下点坐标
    # 第四个参数：（0, 255, 0）是画线对应的rgb颜色
    # 第五个参数：2
    # 是所画的线的宽度

    print('Goodbye world')