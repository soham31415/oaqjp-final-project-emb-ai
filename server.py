"""
This Flask application serves an API endpoint for emotion detection from a text input. 
It uses the EmotionDetection module to process text and return emotions in JSON format.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index page (HTML form) where the user can input text to analyze emotions.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Handles the emotion detection request by retrieving the user's input and
    sending it to the emotion detector function. Returns emotion analysis or
    an error message in case of invalid input.

    Returns:
        Response: A JSON response containing emotion analysis or an error message.
    """
    # Get the text input from the query parameters (because the JS sends it as a URL parameter)
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    # Check if the input is empty (i.e., user didn't provide any text)
    if not text_to_analyze:
        # Return error message for empty input
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    # Call the emotion detector function to get the emotions
    emotion_data = emotion_detector(text_to_analyze)

    if emotion_data['dominant_emotion'] is None:
        # Return error message for invalid text (e.g., unrecognized or incomplete text)
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    # Format the response as per the given specification
    response = {
        "anger": emotion_data['anger'],
        "disgust": emotion_data['disgust'],
        "fear": emotion_data['fear'],
        "joy": emotion_data['joy'],
        "sadness": emotion_data['sadness'],
        "dominant_emotion": emotion_data['dominant_emotion']
    }

    # Return the response in the requested format
    return jsonify(response)

if __name__ == '__main__':
    # Starts the Flask application on the specified host and port.
    app.run(debug=True, host='0.0.0.0', port=5000)
