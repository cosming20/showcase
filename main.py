from flask import Flask, render_template,url_for,jsonify, send_file, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('home.html')

@app.route('/galerie')
def show_gallery():
    return render_template('galerie.html')
    

@app.route('/about')
def gallery_page():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)