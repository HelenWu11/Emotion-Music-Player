def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_face_detection]
    # [START vision_python_migration_image_file]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    # [END vision_python_migration_image_file]

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

import webbrowser
import random
def radio(face):"emotions2的一个元素"
	str x=""
	if face=="anger":
		list anger=["reliefing","relax"]
		final=random.choice(anger)
	else if face=="joy":
		list joy=["party","pop"]
		final=random.choice(joy)
	else if face=="surprise":
		list surprise=["freaking","surprise"]
		final=random.choice(surprise)
	else if face=="sorrow":
		list sorrow=["encouraging","comfort"]
		final=random.choice(sorrow)

	a=webbrowser.get('safari')
	a.open("https://www.youtube.com/results?search_query=music+{}".format(x))
