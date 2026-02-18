import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, headers=headers, json=input_json)
    response_dict = response.json()

    emotions = {
        "anger": response_dict['emotionPredictions'][0]['emotion']['anger'],
        "disgust": response_dict['emotionPredictions'][0]['emotion']['disgust'],
        "fear": response_dict['emotionPredictions'][0]['emotion']['fear'],
        "joy": response_dict['emotionPredictions'][0]['emotion']['joy'],
        "sadness": response_dict['emotionPredictions'][0]['emotion']['sadness'],
    }
    
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions


if __name__ == "__main__":
    print(emotion_detector("I love this new technology."))
