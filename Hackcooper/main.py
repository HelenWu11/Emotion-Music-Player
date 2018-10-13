import logging
import json
from google.cloud import vision
from google.cloud.vision import types
import base64
import re

import webbrowser
import random

from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('Compass.html')

@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
    image_b64 = request.values['photo']
    client = vision.ImageAnnotatorClient()

    image_data = base64.b64decode(re.sub('^data:image/.+;base64,', '', image_b64))
    image = types.Image(content=image_data)
    response_face = client.face_detection(image=image)
    faces = response_face.face_annotations
    likelihood_name = ['UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY']

    #for face in faces:
    #    print("hell it is test of anger\n")
    #    print(face.joy_likelihood)
    #    print("\n")
    d_labels = {}
    for face in faces:
        d_labels["anger"] = face.anger_likelihood;
        d_labels["joy"] = face.joy_likelihood;
        d_labels["surprise"]= face.surprise_likelihood;
        d_labels["sorrow"] = face.sorrow_likelihood;
    max_num = max(d_labels.values())
    final = "NULL"
    if(max_num == d_labels["anger"]):
        anger=["reliefing","relax"]
        final = random.choice(anger)
    if(max_num == d_labels["joy"]):
        joy=["party","pop"]
        final=random.choice(joy)
    if(max_num == d_labels["surprise"]):
        surprise=["freaking","surprise"]
        final=random.choice(surprise)
    if(max_num == d_labels["sorrow"]):
        sorrow=["encouraging","comfort"]
        final=random.choice(sorrow)


    print("\n the answer is"+ final+"lalalalaal\n")
    return json.dumps(final)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
