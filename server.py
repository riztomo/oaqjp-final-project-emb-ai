'''
This is a Docstring
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def home():
    '''
    Docstring
    '''
    return render_template("index.html")

@app.route('/emotionDetector')
def detect_emotion():
    '''
    Docstring
    '''
    result = emotion_detector(request.args.get('textToAnalyze'))

    if result['dominant_emotion'] is not None:

        output = f"""
        For the given statement, the system response is 'anger': {result['anger']},
        'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}
         and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.
        """
    elif result['dominant_emotion'] is None:
        output = "Invalid text! Please try again!"
    else:
        output = "Unknown error"

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
