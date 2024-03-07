from flask import Flask, render_template,url_for,jsonify, send_file, request
from pymongo import MongoClient
from gridfs import GridFS
from PIL import Image
import io
import json
from bson import json_util, ObjectId
import base64


client = MongoClient('mongodb+srv://cosminionutgagea:barbosuetare@cluster0.zcscweb.mongodb.net/')
db = client['PythonProject']
photos = db['photos']
videos = db['videos']
fs = GridFS(db)

app = Flask(__name__)
with open ("image.jpg", "rb") as file:
    image_data = file.read()

fs_files = db.fs.files
fs_chunks = db.fs.chunks
# file_id = fs.put(image_data, filename = "image.jpg")
def  test (id):

    retrieved_image = fs.get(id)
    image = Image.open(io.BytesIO(retrieved_image.read()))
    return image

@app.route('/<media_id>')
def show_image(media_id):
    # Retrieve the image data from MongoDB GridFS
    image_data = fs.get(ObjectId(media_id)).read()

    # Convert the image data to base64 encoding
    base64_image = base64.b64encode(image_data).decode('utf-8')

    # Render the HTML template with the base64-encoded image
    return render_template('image.html', base64_image=base64_image)

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/cascada')
def gallery_page():
    return render_template('gallery.html')

@app.route('/api/media', methods=['GET', 'POST'])
def media():
    if request.method == 'POST':
        # Save uploaded image to MongoDB GridFS
        image = request.files['file']
        filename = image.filename
        image_data = image.read()

        # Save image to MongoDB GridFS
        file_id = fs.put(image_data, filename=filename)
        print("aici")
        return jsonify({"message": "Image uploaded successfully", "file_id": str(file_id)})
    elif request.method == 'GET':
        media = list(db.fs.files.find({}))
        # Convert ObjectId to string for JSON serialization
        for item in media:
            item['_id'] = str(item['_id'])
        # Serialize the list of documents to JSON
        return json_util.dumps(media)

media_ids = [str(file['_id']) for file in fs_files.find()]

print(media_ids)

@app.route('/deleteall')
def delete_all():
    fs_files.delete_many({})
    fs_chunks.delete_many({})
    print("All files deleted from the database.")

@app.route('/medias')
def medias():
    # Retrieve media IDs from the GridFS collection
    media_ids = [str(file['_id']) for file in fs_files.find()]

    # Render the HTML template with media IDs
    return render_template('media.html', media_ids=media_ids)

@app.route('/media/<media_id>')
def get_media_file(media_id):
    # Retrieve the image data from MongoDB GridFS chunks
    chunks = fs.find({"files_id": media_id})
    image_data = b"".join(chunk.raw for chunk in chunks)
    print(test(media_id))
    # Serve the image data as a file response
    return send_file(io.BytesIO(image_data), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)