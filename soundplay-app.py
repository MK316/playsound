import streamlit as st
from pydub import AudioSegment
import io

def convert_to_wav(audio_file):
    # Convert MP3 file to WAV format
    sound = AudioSegment.from_mp3(audio_file)
    buffer = io.BytesIO()
    sound.export(buffer, format="wav")
    buffer.seek(0)
    return buffer

def speed_change(sound, speed=1.0):
    # Change playback speed without changing pitch
    new_frame_rate = int(sound.frame_rate * speed)
    return sound._spawn(sound.raw_data, overrides={'frame_rate': new_frame_rate})

def main():
    st.title('MP3 to WAV Converter and Speed Adjuster')
    audio_file = st.file_uploader("Upload MP3 file", type=['mp3'])

    if audio_file is not None:
        # Play the original MP3 file
        st.audio(audio_file, format='audio/mp3', start_time=0)
        
        # Convert to WAV format
        if st.button('Convert to WAV'):
            wav_buffer = convert_to_wav(audio_file)
            st.success("Conversion successful! Now adjust the playback speed and download or play.")

            # Display a slider for adjusting playback speed
            speed = st.slider("Adjust Speed", 0.5, 2.0, 1.0, step=0.1)
            
            # Load the converted WAV into AudioSegment
            wav_sound = AudioSegment.from_wav(wav_buffer)
            modified_sound = speed_change(wav_sound, speed=speed)
            
            # Export the modified sound to a buffer for playback and download
            mod_buffer = io.BytesIO()
            modified_sound.export(mod_buffer, format="wav")
            mod_buffer.seek(0)
            
            # Play and offer download of the modified sound
            st.audio(mod_buffer, format='audio/wav')
            st.download_button(label="Download Modified WAV",
                               data=mod_buffer,
                               file_name="modified.wav",
                               mime="audio/wav")

if __name__ == "__main__":
    main()
