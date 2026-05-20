"""Flask server for emotion detection."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detection():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze is None:
        return "Bad Request", 400
    response = emotion_detector(text_to_analyze)
    emotion = response
    return (
        f"For the given statement, the system response is "
        f"'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, "
        f"'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and "
        f"'sadness': {emotion['sadness']}. "
        f"The dominant emotion is {emotion['dominant_emotion']}."
)

@app.route("/")
def render_index_page():
    """Detect emotions from input text and return results."""
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
