import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    formatted_response = json.loads(response.text)
    emotion_dict = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict
