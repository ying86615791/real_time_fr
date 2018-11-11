# Real time face recognition
Face detector and feature extractor are implemented by Tensorflow.

## Installation:
    1. conda create -n tfpy3 python=3.6
    2. source activate tfpy3
    3. pip install tensorflow-gpu
    4. pip install opencv-contrib-python
    5. pip install scipy pillow matplotlib 
    6. Download the pretrained models (see folder "/models", for default: "/models/model-20180402-114759.ckpt-27").
    7. python main.py

    for web
    8. pip install flask (flask_sockets)
    9. sudo apt-get install nginx
    10. sudo apt-get install build-essential python-dev
    11. sudo pip install uwsgi


## References:
- The codes refer to [FaceRec](https://github.com/vudung45/FaceRec), which refers to [facenet](https://github.com/davidsandberg/facenet)
- Face detector: [MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/index.html)
- Face feature extractor: [FaceNet](https://github.com/davidsandberg/facenet)
