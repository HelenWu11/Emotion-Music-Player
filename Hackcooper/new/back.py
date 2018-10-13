import logging
import json
from google.cloud import vision
from google.cloud.vision import types
import base64
import re

from flask import Flask, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('bytemakeup.html')

@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
    print("********************\ntest**********************\n")
    image_b64 = request.values['photo']
    client = vision.ImageAnnotatorClient()

    image_data = base64.b64decode(re.sub('^data:image/.+;base64,', '', image_b64))
    image = types.Image(content=image_data)
    response_label = client.label_detection(image=image)
    labels = response_label.label_annotations

    for tmp in labels:
        print(tmp.description)

    d_labels = {}
    print(labels)
    eyebrow = False
    eyelash = True
    lip = False
    freckle = False
    wrinkle = False

    for des in labels:
        if des.description=="eyebrow":
            eyebrow =True
            d_labels["eyebrow"]="https://www.elle.com/beauty/makeup-skin-care/tips/g8496/how-to-define-eyebrows/"
        elif des.description== "lip":
            lip = True
            d_labels["lip"]="https://www.youtube.com/watch?v=wYzg8HgPCHI"
        elif des.description== "eyelash":
            eyelash = False
        elif des.description== "freckle":
            freckle= True
            d_labels["freckle"]="https://www.youtube.com/watch?v=i3WaHqaJ8U0"
        elif des.description== "wrinkle":
            wrinkle = True
            d_labels["wrinkle"]="https://www.youtube.com/watch?v=a0RLT68Z-w0"

    if eyelash ==True:
        d_labels["eyelash"]="https://www.youtube.com/watch?v=TfxJCQfcMkk"
    if eyebrow == False:
        d_labels["eyebrow"]="http://www.rafichowdhury.com/eyebrows-types/"
    if lip==False:
        d_labels["lip"]="https://www.byrdie.com/types-of-lipstick/slide4"
    if freckle==False:
        d_labels["freckle"]="https://blog.reneerouleau.com/how-to-prevent-summer-sun-spots/"
    if wrinkle==False:
        d_labels["wrinkle"]="https://www.siobeauty.com/blogs/news/how-to-prevent-wrinkles"

    return json.dumps({'labels': d_labels,'faces': ""});

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
    print("************************\n Hello world\n***************")
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
