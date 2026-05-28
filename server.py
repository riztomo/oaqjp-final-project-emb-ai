from flask import Flask, jsonify, render_template
import requests

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
