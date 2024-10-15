import streamlit as st
from pydub import AudioSegment
import io

def speed_change(sound, speed=1.0):
    new_frame_rate = int(sound.frame_rate * speed)
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_frame_rate})

def main():
    st.title("Audio Speed Adjuster")
    uploaded_file = st.file_uploader("Upload an audio file", type=['wav'])  # Limit to WAV files

    if uploaded_file is not None:
        try:
            sound = AudioSegment.from_file(uploaded_file)
            speed = st.slider("Adjust Speed", 0.5, 2.0, 1.0, step=0.1)
            modified_sound = speed_change(sound, speed=speed)

            buffer = io.BytesIO()
            modified_sound.export(buffer, format="wav")
            buffer.seek(0)
            st.audio(buffer, format='audio/wav')
        except Exception as e:
            st.error(f"An error occurred: {e}. Please ensure the file is a WAV format.")

if __name__ == "__main__":
    main()
