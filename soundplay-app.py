import streamlit as st
from pydub import AudioSegment
import io

# Function to change playback speed
def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def main():
    st.title("Audio Speed Adjuster")
    
    # File uploader allows user to add their own audio
    uploaded_file = st.file_uploader("Upload WAV files", type=['wav'])
    if uploaded_file is not None:
        sound = AudioSegment.from_file(uploaded_file)
        
        # Slider to adjust the speed
        speed = st.slider("Select playback speed", 0.5, 2.0, 1.0, 0.1)
        altered_sound = speed_change(sound, speed=speed)
        
        # Export altered sound to a byte buffer and then play it
        buffer = io.BytesIO()
        altered_sound.export(buffer, format="wav")
        buffer.seek(0)
        
        st.audio(buffer, format='audio/wav', start_time=0)

if __name__ == "__main__":
    main()
