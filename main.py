from flask import Flask, render_template,url_for,jsonify, send_file
from pymongo import MongoClient
from gridfs import GridFS
from PIL import Image
import io
import json
client = MongoClient("")


client = MongoClient('mongodb+srv://cosminionutgagea:barbosuetare@cluster0.zcscweb.mongodb.net/')
db = client['PythonProject']
photos = db['photos']
videos = db['videos']
fs = GridFS(db)

app = Flask(__name__)
with open ("image.jpg", "rb") as file:
    image_data = file.read()


file_id = fs.put(image_data, filename = "image.jpg")

retrieved_image = fs.get(file_id)
image = Image.open(io.BytesIO(retrieved_image.read()))
image.show()

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/cascada')
def gallery_page():
    return render_template('gallery.html')

@app.route('/api/media')
def get_media():
    # Retrieve photos and videos from MongoDB
    media = list(db.media.find({}))
    return jsonify(media)

@app.route('/media/<media_id>')
def get_media_file(media_id):
    # Retrieve the media file from MongoDB GridFS
    media_file = fs.get(media_id)
    # return send_file(media_file, mimetype=media_file.content_type)
    return send_file(io.BytesIO(media_file.read()), mimetype=media_file.content_type)

if __name__ == '__main__':
    app.run(debug=True)