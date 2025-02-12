import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig, XttsArgs
from TTS.config.shared_configs import BaseDatasetConfig
import sounddevice as sd
import numpy as np
import langid

# Allow loading full checkpoint
torch.serialization.default_load_weights_only = False

# Add safe globals
torch.serialization.add_safe_globals([XttsConfig, XttsAudioConfig, BaseDatasetConfig, XttsArgs])

# check device
device = "cuda" if torch.cuda.is_available() else "cpu"
class SpeakBot:
    def __init__(self, tts_model="tts_models/multilingual/multi-dataset/xtts_v2", gpu=True):
        print(f"Using device: {device}")
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
        self.tts.to(device)

    def split_by_language(self, text):
        words = text.split()
        segments = []
        current_lang = None
        current_segment = ""

        for word in words:
            lang, _ = langid.classify(word)  # Detect language per word
            if lang != current_lang:
                if current_segment:
                    segments.append((current_segment.strip(), current_lang))
                current_segment = word
                current_lang = lang
            else:
                current_segment += " " + word

        if current_segment:
            segments.append((current_segment.strip(), current_lang))

        return segments

    def generate_speech(self, text):
        # Get text segments with detected languages
        text_segments = self.split_by_language(text)

        # Initialize array to store audio
        audio_clips = []
        sample_rate = None

        # Process each segment separately
        for segment_text, lang in text_segments:
            print(f"Processing '{segment_text}' as language '{lang}'")

            # Convert langdetect's output to TTS-compatible language names
            language_name = "en" if lang == "en" else "zh"
            speaker_wav = '/home/set/Projects/python-projects/chat-bot/set_voice.wav'
            # Generate speech for this segment
            try:
                audio_data = self.tts.tts(
                    text=segment_text,
                    speaker_wav=speaker_wav,
                    language=language_name
                )
            except Exception as e:
                print(f"Error generating speech for segment '{segment_text}': {e}")
                continue

            # Store audio data
            audio_clips.append(audio_data)
        
        # Check if audio_clips is empty
        if len(audio_clips) == 0:
            raise ValueError("No audio data generated for the text segments.")

        # Concatenate all audio segments
        final_audio = np.concatenate(audio_clips)

        return final_audio, self.tts.synthesizer.output_sample_rate
    
    def text_direct_to_speech(self, text, language="en"):
        speaker_wav = '/home/set/Projects/python-projects/chat-bot/set_voice.wav'
        audio_data = self.tts.tts(
            text=text,
            speaker_wav=speaker_wav,
            language=language
            )
        return audio_data, self.tts.synthesizer.output_sample_rate

    def play_speech(self, audio_data, sample_rate):
        # Play the generated speech
        sd.play(audio_data, samplerate=sample_rate)
        sd.wait()  # Wait until playback finishes
    
    def stop_speech(self):
        # Stop the audio playback
        sd.stop()

# Example usage
if __name__ == "__main__":
    speak_bot = SpeakBot()
    text = "Hello, welcome to the world of AI."
    try:
        audio_data, sample_rate = speak_bot.generate_speech(text)
        speak_bot.play_speech(audio_data, sample_rate)
    except ValueError as e:
        print(f"Error: {e}")
    # To stop the audio playback, you can call speak_bot.stop_speech()