import streamlit as st
from pydub import AudioSegment
from pydub.playback import play
import io

# Function to change playback speed
def speed_change(sound, speed=1.0):
    # Change the frame rate. This changes the speed but keeps the pitch the same.
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

# Streamlit widgets to interact with the sound file
st.title('Sound Speed Adjuster')
uploaded_file = st.file_uploader("Choose a sound file", type=['mp3', 'wav'])

# Only run the rest of the code if the file is uploaded
if uploaded_file is not None:
    # Load the audio file
    file_buffer = io.BytesIO(uploaded_file.read())
    sound = AudioSegment.from_file(file_buffer)

    # Slider for selecting speed
    speed = st.slider("Select playback speed", 0.5, 2.0, 1.0, 0.1)
    
    # Adjusting the sound speed
    modified_sound = speed_change(sound, speed=speed)
    
    # Save the modified file to a temporary buffer
    modified_file_buffer = io.BytesIO()
    modified_sound.export(modified_file_buffer, format="wav")
    modified_file_buffer.seek(0)

    # Display a button to play the modified sound
    if st.button('Play modified sound'):
        play(modified_sound)

# Additional instructions for using the application in local setup
st.write("Note: Due to limitations in Google Colab, audio playback is not supported here. \
          Run this script locally in your environment to test audio playback.")
