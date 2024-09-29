from flask import Flask, request, jsonify
import numpy as np
import soundfile as sf
import torch
from wisher_model import WisherTTS  # Replace with the actual import for your model

app = Flask(__name__)

# Load the Wisher TTS model
model = WisherTTS()
model.load_pretrained('path/to/pretrained/model')  # Adjust the path as necessary

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Generate audio
    audio = model.generate_audio(text)
    
    # Save audio to a file
    audio_file_path = 'output.wav'
    sf.write(audio_file_path, audio.numpy(), 22050)  # Adjust sample rate if needed

    return jsonify({'message': 'Audio synthesized', 'audio_file': audio_file_path}), 200

if __name__ == "__main__":
    app.run(debug=True)
