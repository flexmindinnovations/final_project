"""
Flask web server for emotion detection application.
Provides routes for index page and emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index.html page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Detect emotions from the given text query parameter.
    Returns formatted response or error message for blank input.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
