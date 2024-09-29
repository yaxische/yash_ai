import pyttsx3

engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

# Print available voice IDs and descriptions
print("Available voices:")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.id} - {voice.name} ({voice.languages})")

# Choose a voice by ID (replace 'ID' with the desired voice ID)
selected_voice_id = 'ID' # Replace 'ID' with the actual ID of your choice 
engine.setProperty('voice', selected_voice_id)

# Text to speech conversion
text = "Hello, world! This is a text to speech example."
engine.say(text)

# Run the speech engine
engine.runAndWait()