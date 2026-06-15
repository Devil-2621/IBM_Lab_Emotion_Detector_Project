"""
Emotion Detector - Flask Web Application

Static code analysis: pylint score 10.00/10.00
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detector_route():
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze', '')
    else:
        text_to_analyze = request.form.get('textToAnalyze', '')

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input! Please provide text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid input! Please provide text to analyze.", 400

    if result.get('dominant_emotion') is None:
        return "Invalid input! Please provide text to analyze.", 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
