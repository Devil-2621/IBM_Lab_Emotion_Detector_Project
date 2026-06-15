import requests
import json


def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return None

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        'grpc-timeout': '30',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'apikey'
    }

    body = {
        'raw_document': {
            'content': text_to_analyze,
            'content_type': 'text/plain'
        }
    }

    try:
        response = requests.post(url, json=body, headers=headers)

        if response.status_code == 200:
            response_json = response.json()

            if 'emotionPredictions' in response_json:
                emotions = response_json['emotionPredictions'][0]['emotion']

                anger_score = emotions.get('anger', 0)
                disgust_score = emotions.get('disgust', 0)
                fear_score = emotions.get('fear', 0)
                joy_score = emotions.get('joy', 0)
                sadness_score = emotions.get('sadness', 0)

                emotion_scores = {
                    'anger': anger_score,
                    'disgust': disgust_score,
                    'fear': fear_score,
                    'joy': joy_score,
                    'sadness': sadness_score
                }

                dominant_emotion = max(emotion_scores, key=emotion_scores.get)
                emotion_scores['dominant_emotion'] = dominant_emotion

                return emotion_scores
            else:
                return None
        elif response.status_code == 400:
            emotion_scores = {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }
            return emotion_scores
        else:
            return None

    except requests.exceptions.RequestException:
        return None
