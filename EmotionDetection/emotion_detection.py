import requests
import json
from typing import Dict

def emotion_detector(text_to_analyze: str) -> Dict[str, float | str]:
    # Check if the input text is blank
    if not text_to_analyze.strip():
        # Return the emotion data with None values for all keys
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    # Send the request to the API
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        predictions = response_json.get("emotionPredictions", [])
        
        if predictions:
            emotions = predictions[0]["emotion"]
            # Extract required emotions
            relevant_emotions = {emotion: emotions[emotion] for emotion in ["anger", "disgust", "fear", "joy", "sadness"]}
            # Find dominant emotion
            dominant_emotion = max(relevant_emotions, key=relevant_emotions.get)
            # Add dominant emotion to dictionary
            relevant_emotions["dominant_emotion"] = dominant_emotion
            return relevant_emotions
        else:
            return {"error": "No emotion detected"}
    else:
        return {"error": f"API request failed with status code {response.status_code}"}
