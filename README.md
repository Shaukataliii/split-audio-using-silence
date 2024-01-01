## split-audio-using-silence
This code split audios based on silence and saves them.

### Usage
1. Give the function a path of the folder containing audio files in wav format.
2. Give the output folder path
3. Now run the file. It will loop through all the wav files present in the input folder and for each file it creates a new folder in the output folder direcotory and splits the files based on silence and then saves all of its chunks in that newly created folder. It follows the following naming convention.
   
Name of the folder:  {audio_file_name}
Name of the chunk:  {audio_file_name_chunkNo}
