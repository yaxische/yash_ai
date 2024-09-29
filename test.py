from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)

# Load the Whisper model (using the correct method)
model = whisper.load_model()  # Choose a model size: "tiny", "base", "small", "medium", "large"

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    try:
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Missing text parameter'}), 400

        audio = whisper.load_audio(text)
        options = whisper.DecodingOptions()
        result = whisper.decode(model, audio, options)

        audio_file_path = result["segments"][0]["audio_file"]
        
        # You can choose how to handle the audio file:
        # 1. Return the audio file path (requires client to handle playback)
        return jsonify({'audio_file': audio_file_path})
        # 2. Encode the audio and return as base64 (client needs to decode)
        # import base64
        # with open(audio_file_path, 'rb') as f:
        #     audio_data = f.read()
        #     audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        #     return jsonify({'audio_base64': audio_base64})
        # 3. Use a library like `playsound` and stream the audio (requires a server setup)
        # ...

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)