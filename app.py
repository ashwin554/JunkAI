from flask import Flask, render_template, request
from sql import insertGarbageDump
import sqlite3
app = Flask(__name__,template_folder='./template')



@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
   


    image = request.files['image']
    image.save('./image.jpg')
    location = request.form['text']
    print(location)
    print(type(image))
    a=predictGar(image)
    if a=='garbage':
        insertGarbageDump(location)
        return render_template("index.html",prediction="Garbage detected at "+location+" and reported successfully")
    else:
        return render_template("index.html",prediction="No Garbage detected at "+location)
    # Process the image and text here
    
    # return render_template('index.html', prediction=a)


def predictGar(image):
    from inference_sdk import InferenceHTTPClient

    CLIENT = InferenceHTTPClient(
        api_url="https://classify.roboflow.com",
        api_key="yMSUdaNkSjIbtYbBnumP"
    )

    result = CLIENT.infer('./image.jpg', model_id="garbage-detection-nnyof/1")
    print(result)
    return result['top']



@app.route('/details')
def details():
    conn = sqlite3.connect('garbage.db')
    cursor = conn.execute("SELECT * FROM garbagedump")
    data = cursor.fetchall()
    conn.close()
    return render_template('db.html', data=data)


if __name__ == '__main__':
    app.run()