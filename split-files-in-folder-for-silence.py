import os, silence
from pydub import AudioSegment

# The function takes a folder of wav files and splits each file based on silence
# of 01s, converts that to 1 channel and then creates a new folder with the name of the audio file and then saves
# all the chunks in that folder with naming convention file_name_chunkNo
def split_audio_on_silence_and_save(input_folder, output_folder, silence_threshold=-40, min_silence_duration=1000):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over each WAV file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            input_file_path = os.path.join(input_folder, filename)

            # Load the audio file
            audio = AudioSegment.from_file(input_file_path)

            # Split the audio based on silence
            chunks = silence.split_on_silence(audio, silence_thresh=silence_threshold, min_silence_len=min_silence_duration)

            # Create a subfolder in the output folder with the name of the original audio file
            file_output_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
            if not os.path.exists(file_output_folder):
                os.makedirs(file_output_folder)

            # Save each chunk using the specified naming convention
            for i, chunk in enumerate(chunks):
                chunk = chunk.set_channels(1)
                output_file_name = f"{os.path.splitext(filename)[0]}_{i + 1}.wav"
                output_file_path = os.path.join(file_output_folder, output_file_name)
                chunk.export(output_file_path, format="wav")

        else:
            print('Given file is not a .wav file:', filename)


# calling the function to split the audios based on silence and save them.
input_folder = "/content/wav-files"
output_folder = "/content/silence-segments"
split_audio_on_silence_and_save(input_folder, output_folder)