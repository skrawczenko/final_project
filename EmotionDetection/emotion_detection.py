import requests 
import json

def emotion_detector(text_to_analyse):

  emotion_template = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

  if not text_to_analyse:
      print("Invalid text! Please try again!.")
      return emotion_template
  else:
      url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
      myobj = { "raw_document": { "text": text_to_analyse } } 
      header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
      response = requests.post(url, json = myobj, headers=header)   
      if response.status_code != 200:
          return emotion_template
      formatted_response = json.loads(response.text)
      emotion = formatted_response['emotionPredictions'][0]['emotion'] 
      dominant = max(emotion, key=emotion.get)
      emotion['dominant_emotion'] = dominant
  return emotion 
