# Real time face recognition
Face detector and feature extractor are implemented by Tensorflow.

## Installation:
    1. conda create -n tfpy3 python=3.6
    2. source activate tfpy3
    3. pip install tensorflow-gpu
    4. pip install opencv-contrib-python
    5. pip install scipy,pillow


    1. Install opencv3, tensorflow and etc.
    2. Download the pretrained models (see folder "/models", for default: "/models/model-20180402-114759.ckpt-27").
    3. python main.py

## References:
- The codes refer to [FaceRec](https://github.com/vudung45/FaceRec), which refers to [facenet](https://github.com/davidsandberg/facenet)
- Face detector: [MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html)
- Face feature extractor: [FaceNet](https://github.com/davidsandberg/facenet)
