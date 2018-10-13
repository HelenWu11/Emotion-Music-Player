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
    likelihood_name = ['UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY']



dict={};
for face in faces:
    dict[face]["anger"]=likelihood_name[face.anger_likelihood];
    dict[face]["joy"]=likelihood_name[face.joy_likelihood];
    dict[face]["surprise"]=likelihood_name[face.surprise_likelihood];
    dict[face]["sorrow"]=likelihood_name[face.sorrow_likelihood];

def emotionjudge(faces):
    dict2={};
    int c=0;
    list emotionsnumbers=[];
    emotions=["anger","joy","surprise","sorrow"]
    emotions2=[];
    for face in dict:
        for emotion in dict[face]:
        if dict[face][emotion]=='UNKNOWN':
            c=1;
            dict2[face][emotion]=c;
            emotionsnumbers.append(c);
        else if dict[face][emotion]=='VERY_UNLIKELY':
            c=2;
            dict2[face][emotion]=c;
            emotionsnumbers.append(c);
        else if dict[face][emotion]=='UNLIKELY':
            c=3;
            dict2[face][emotion]=c;
            emotionsnumbers.append(c);
        else if dict[face][emotion]=='POSSIBLE':
            c=4;
            dict2[face][emotion]=c;
            emotionsnumbers.append(c);
        else if dict[face][emotion]=='LIKELY':
            c=5;
            dict2[face][emotion]=c;
            emotionsnumbers.append(c);
        else:
            c=6;
            emotionsnumbers.append(c);
            dict2[face][emotion]=c;
    int count =0
    for number in emotionsnumbers:
        if number== max(emotionsnumbers):
            emotions2.append(emotions[count]);
        count ++;
    if len(emotions>1):
        "输出全部结果一个for loop"
    else：
    "输出一个结果"


