from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')
@app.route("/emotionDetector")
def emtn_detector():
    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)
    if result['dominant_emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"
    # Build formatted response
    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )
    return response_string

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)
