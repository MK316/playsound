import streamlit as st
from pydub import AudioSegment
import io

def speed_change(sound, speed=1.0):
    """Function to change the playback speed of the audio file."""
    # Adjusting frame rate while maintaining the same number of frames.
    new_frame_rate = int(sound.frame_rate * speed)
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_frame_rate})

def main():
    st.title("Audio Speed Adjuster")
    uploaded_file = st.file_uploader("Upload an audio file", type=['wav', 'mp3', 'ogg'])

    if uploaded_file is not None:
        sound = AudioSegment.from_file(uploaded_file)
        speed = st.slider("Adjust Speed", 0.5, 2.0, 1.0, step=0.1)
        modified_sound = speed_change(sound, speed=speed)

        # Preparing audio for playback
        buffer = io.BytesIO()
        modified_sound.export(buffer, format="wav")
        buffer.seek(0)
        st.audio(buffer, format='audio/wav')

if __name__ == "__main__":
    main()
