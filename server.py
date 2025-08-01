from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(Emotion Detector)

@app.route("/emotionDetector")
def emtn_detector():
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return "Error: No text provided", 400

    result = emotion_detector(text_to_analyse)

    # Build formatted response
    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
