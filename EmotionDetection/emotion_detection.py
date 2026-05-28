import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=input_json, headers=headers)
    dictionary = json.loads(response.text)

    emotion = dictionary['emotionPredictions'][0]['emotion']
    collection = ['anger', 'disgust', 'fear', 'joy', 'sadness']

    largest_value = 0
    largest_key = ''

    for k in collection:
        if largest_value < emotion[k]:
            largest_value = emotion[k]
            largest_key = k
        else:
            continue

    emotion['dominant_emotion'] = largest_key

    return emotion