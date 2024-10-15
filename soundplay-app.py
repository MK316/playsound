import io
from pydub import AudioSegment
from IPython.display import Audio

# Function to change playback speed
def speed_change(sound, speed=1.0):
    # Speed changes could be done by modifying the frame rate.
    # This changes the speed without changing the pitch.
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# Load an audio file (modify path as needed)
audio_path = "path_to_your_audio_file.wav"
sound = AudioSegment.from_file(audio_path)

# Change the speed of the audio (1.5 times the original speed)
altered_sound = speed_change(sound, speed=1.5)

# Export altered sound to a byte buffer
buffer = io.BytesIO()
altered_sound.export(buffer, format="wav")
buffer.seek(0)

# Play the altered sound
Audio(buffer.read(), rate=altered_sound.frame_rate)
