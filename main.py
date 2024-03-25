from flask import Flask, render_template,url_for,jsonify, send_file, request
from pymongo import MongoClient
from gridfs import GridFS
from PIL import Image
import io
import json
from bson import json_util, ObjectId
import base64

# https://imgur.com/a/Tn38oJ5

client = MongoClient('mongodb+srv://cosminionutgagea:barbosuetare@cluster0.zcscweb.mongodb.net/')
db = client['PythonProject']
photos = db['photos']
videos = db['videos']


app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/galerie')
def show_gallery():
    return render_template('galerie.html')
    

@app.route('/cascada')
def gallery_page():
    return render_template('gallery.html')

@app.route('/image_details/<image_id>')
def image_details(image_id):
    # Your logic to retrieve details of the image with the given ID
    # This could involve querying your database or performing other operations
    # For demonstration purposes, let's just return a simple message
    return f"Details for image with ID {image_id}"

@app.route('/galerie')
def galerie():
    return render_template('galerie.html')



if __name__ == '__main__':
    app.run(debug=True)