# app.py
from flask import Flask, render_template, request, jsonify
import os
import tensorflow as tf 
import keras
from keras.utils import load_img, img_to_array 
import numpy as np
from PIL import Image
import requests
import json
from datetime import datetime
import sqlite3
import base64
from io import BytesIO

import our_model
import feature_extract
import test_tts



#Flask 객체 인스턴스 생성
app = Flask(__name__)
# model = tf.keras.models.load_model('dog_cat_model.h5')
flag=0
print(flag)
def read_img(fname) :
  img = load_img(fname , target_size=(150,150))
  x = img_to_array(img) 
  images = np.expand_dims(x, axis=0)
  images = images.astype('float')
  images = images / 255.0
  return images


# naver papago open api 
def translate(text, source='en', target='ko'):
    CLIENT_ID, CLIENT_SECRET = 'iICkLuA8cumOEp9WwpWR', 'qJyQVZ7yNj'
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    headers = {
        'Content-Type': 'application/json',
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    data = {'source': 'en', 'target': 'ko', 'text': text}
    response = requests.post(url, json.dumps(data), headers=headers)
    
    print("translation on Process")
    return response.json()['message']['result']['translatedText']

  
@app.route('/service',methods=('GET', 'POST')) #url
def index():
    return render_template('service.html')

@app.route('/')  
def home():
    filename = 'Image20230428091930.png'
    file_path = os.path.join('static',filename)
    return render_template('home.html' , file_path = file_path)

@app.route('/project')  
def project():
    return render_template('project.html')

@app.route('/predict', methods=['GET','POST'])
def upload():
       
    global caption_model, CNN_Encoder, flag 

    if flag ==0: 
        caption_model = our_model.define_our_model()
        our_model.load_model(caption_model)
        CNN_Encoder = feature_extract.define_CNN_Encoder()
        flag +=1 

    if request.method == 'POST':
        
        current_time = datetime.now()
        timestamp = int(current_time.timestamp())
        
        id_key = '90'+str(timestamp)
        id_key = int(id_key)
        
        file = request.files['image']

        filename = file.filename
        filename, extension = os.path.splitext(file.filename)
        filename = str(id_key)
        new_filename = filename + '.jpg'
        

          

        # file.save(os.path.join('static', filename))
        file_path = os.path.join('static/images',new_filename)
        file.save(file_path)
        images = read_img(file_path)
       

        
         # insert the image data into SQLite
         #DB 연동 테스트
        # conn = sqlite3.connect('coco30k_F_v4.db')
        # cursor = conn.cursor()
        # cursor.execute("INSERT INTO customer_image VALUES (?, ?, ?)", (id_key, bi_img, timestamp))
        # conn.commit()
        # conn.close()
        # features

        
        # feature = feature_extract.extract_features(file_path, CNN_Encoder)
        # print(type(feature), feature.shape)
        pred = feature_extract.extract_caption(file_path,caption_model,CNN_Encoder)

        # trans = "대기"
        trans = translate(pred[7:-5])
        test_tts.create_tts_to_en(pred[7:-5])
        test_tts.create_tts_to_ko(trans)
        audio_file_en = 'static/audios/output_en.mp3'
        audio_file_ko = 'static/audios/output_ko.mp3'
        
        
    return render_template('predict.html', fileimg = file_path , pred = pred[7:-5], id_key = id_key, trans = trans , audio_file_en = audio_file_en , audio_file_ko = audio_file_ko)
@app.route('/about')  
def about():
    return render_template('about.html')    

if __name__=="__main__":
  app.run(debug=True)
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
  # app.run(host="0.0.0.0", port="9000", debug=True) #aws