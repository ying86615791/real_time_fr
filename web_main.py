#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from main import FR_Service, FRwithrects
import numpy as np
import io
import re
import base64
from flask import Flask, request, render_template, jsonify
from flask_sockets import Sockets
from PIL import Image, ImageDraw, ImageFont

FRS = FR_Service()
app = Flask(__name__)
app.config.update(PORT=5001)
# app.config.update(HOST='0.0.0.0')
# sockets = Sockets(app)

def url2pilimg(base64_url):
    base64_string = re.sub('^data:image/.+;base64,', '', base64_url)
    imgdata = base64.b64decode(str(base64_string))
    pil_img = Image.open(io.BytesIO(imgdata))
    return pil_img

def pilimg2url(pil_img):
    buff = io.BytesIO()
    pil_img.save(buff, format="JPEG")
    new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")
    return new_image_string

def drawbox(img, rects, ann):
    """
    :param img: numpy array
    :param rects:
    :param ann: recog_data from frwithrects
    :return: PIL img with face boxes
    """
    pim = Image.fromarray(img)
    draw = ImageDraw.Draw(pim)
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", size=20)
    for (i,rect) in enumerate(rects):
        # plot face
        face_x = rect[0]
        face_y = rect[1]
        face_width = rect[2]
        face_height = rect[3]
        draw.rectangle(((face_x, face_y), (face_x+face_width, face_y+face_height)), fill=None)
        if ann is not None:
            str_displayed = ann[i][0] + "\n" + str(100 * round(ann[i][1], 4)) + "%"
            draw.text((face_x, face_y + 0.05 ), str_displayed, font=font)
    # pim.show()
    return pim

@app.route('/')
def index():
    result = {'result': 'Hello World'}
    return render_template("index.html",
                           title = 'Home',
                           result = result)

@app.route('/fr',methods=["POST", 'GET']) # methods=["POST", 'GET']
def real_time_fr():
    global FRS
    # print("real_time_fr")
    if request.method == 'POST':
        # print(request.method)
        base64_url = request.form['image']
    elif request.method == 'GET':
        # print(request.method)
        base64_url = request.args.get('image')
    else:
        base64_url = None
    if base64_url is not None:
        pilimg = url2pilimg(base64_url)
        img = np.array(pilimg)

        # 人脸检测
        rects, landmarks = FRS.face_detector.detect_face(img,40)
        if len(rects)!=0:
            # 提取特征
            recog_data = FRwithrects(FRS, img, rects, landmarks)
            # 在原图上画框
            out_pim = drawbox(img, rects, ann=recog_data)
        else: # 没有检测到则返回原图
            out_pim = pilimg
        # out_pim = pilimg
        out_img_url = pilimg2url(out_pim)
    else:
        out_img_url = 'None'
    result = {'data': out_img_url}
    return jsonify(result)

# @sockets.route('/fr')
# def echo_socket(ws):
#     while not ws.closed:
#         message = ws.receive()
#         # print(message)
#         ws.send(message)

if __name__ == '__main__':
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    # server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    # print('begin gevent server')
    # server.serve_forever()
    print('begin flask debug')
    app.run(debug=False, threaded=False, port=5000)