'''
@Author: David Vu
Run the pretrained model to extract 128D face features
copy from vudung45, but vudung45 use model from davidsandberg
vudung45: FaceRec, https://raw.githubusercontent.com/vudung45/FaceRec/master/architecture/inception_resnet_v1.py
davidsandberg: facenet, https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py

'''

import tensorflow as tf
from architecture import inception_resnet_v1 as resnet
import numpy as np

class FaceFeature(object):
    def __init__(self, face_rec_graph, model_path = 'models/model-20180402-114759.ckpt-275'):
        '''
        model-20170512-110547.ckpt-250000     bottleneck_layer_size=128
        model-20180402-114759.ckpt-275        bottleneck_layer_size=512
        :param face_rec_sess: FaceRecSession object
        :param model_path:
        '''
        print("Loading model...")
        with face_rec_graph.graph.as_default():
            self.sess = tf.Session()
            self.x = tf.placeholder('float', [None,160,160,3]); #default input for the NN is 160x160x3
            self.embeddings = tf.nn.l2_normalize(
                                        resnet.inference(self.x, 0.6, phase_train=False, bottleneck_layer_size=512)[0], 1, 1e-10); #some magic numbers that u dont have to care about

            saver = tf.train.Saver() #saver load pretrain model
            saver.restore(self.sess, model_path)
            print("Model loaded")


    def get_features(self, input_imgs):
        images = load_data_list(input_imgs,160)
        return self.sess.run(self.embeddings, feed_dict = {self.x : images})



#some image preprocess stuff
def prewhiten(x):
    mean = np.mean(x)
    std = np.std(x)
    std_adj = np.maximum(std, 1.0 / np.sqrt(x.size))
    y = np.multiply(np.subtract(x, mean), 1 / std_adj)
    return y

def load_data_list(imgList, image_size, do_prewhiten=True):
    images = np.zeros((len(imgList), image_size, image_size, 3))
    i = 0
    for img in imgList:
        if img is not None:
            if do_prewhiten:
                img = prewhiten(img)
            images[i, :, :, :] = img
            i += 1
    return images