from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/')
def index():
    return "Welcome to the Football Stars Image Classification API!"

@app.route('/favicon.ico')
def favicon():
    # You can return an actual favicon file here
    return "", 204

if __name__ == "__main__":
    print("Starting Python Flask Server For Football Stars Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)