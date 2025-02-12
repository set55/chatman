import speech_recognition as sr
import whisper

class ListenBot:
    def __init__(self, model_name="base"):
        # Initialize the Whisper model
        self.model = whisper.load_model(model_name)
        # Initialize the recognizer
        self.recognizer = sr.Recognizer()
        # temp audio file path
        self.audio_file = "temp.wav"

    def listen(self, source):
        # Adjust for ambient noise and record the audio
        audio = self.recognizer.listen(source)
        print("Done listening.")

        # Save the audio to a temporary file
        filePath = "temp.wav"
        with open(filePath, "wb") as f:
            f.write(audio.get_wav_data())
        text = self.transcribe(filePath)
        print("Transcribed text:", text)
        return text


    
    def transcribe(self, audio_file):
        # Transcribe the audio using Whisper
        result = self.model.transcribe(audio_file)
        return result["text"]
    
    def get_texts(self):
        return self.text

# Example usage
if __name__ == "__main__":
    listen_bot = ListenBot()
    with sr.Microphone() as source:
        print("Speak microphone...")
        while True:
            text = listen_bot.listen(source)
            if text:
                print(f"Text detected: {text}")