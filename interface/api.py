from customer_segmentation import main
import flask
import os
from flask_cors import CORS
from flask import Flask, request, jsonify, stream_with_context, Response
import os
import base64


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/images', methods= ['POST','GET'])
def get_images():
    images_dir = 'temp_files'
    #run = main.get_plots(file)
    print('ss')
    images = []
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            with open(os.path.join(images_dir, filename), 'rb') as f:
                image = base64.b64encode(f.read()).decode('utf-8')
                images.append(image)
    return jsonify(images)

@app.route('/get3dplots')
def get_3d_plots():
    with open('temp_files/3d_plot.html', 'rb') as file:
        data = file.read()
    decoded_data = data.decode('utf-8')
    return decoded_data

app.run(host="127.0.0.1", port=5001, debug=False)