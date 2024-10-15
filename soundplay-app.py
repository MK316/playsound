import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import io

def speed_change(sound, speed=1.0):
    """Function to change the playback speed of the audio file."""
    # Adjusting frame rate while maintaining the same number of frames.
    new_frame_rate = int(sound.frame_rate * speed)
    sound_with_changed_speed = sound._spawn(sound.raw_data, overrides={'frame_rate': new_frame_rate})
    return sound_with_changed_speed

def main():
    st.title("Audio Speed Adjuster")
    uploaded_file = st.file_uploader("Upload an audio file", type=['mp3', 'wav', 'ogg'])

    if uploaded_file is not None:
        # Read the uploaded file into AudioSegment compatible format
        file_format = uploaded_file.name.split('.')[-1]
        sound = AudioSegment.from_file(uploaded_file, format=file_format)
        
        # Slider to adjust the speed
        speed = st.slider("Adjust Speed", 0.5, 2.0, 1.0, step=0.1)
        
        # Apply the speed change function
        modified_sound = speed_change(sound, speed=speed)
        
        # Export the modified sound to a byte buffer
        buffer = io.BytesIO()
        modified_sound.export(buffer, format="wav")
        buffer.seek(0)

        # Use st.audio to play the modified sound
        st.audio(buffer, format='audio/wav')

if __name__ == "__main__":
    main()
