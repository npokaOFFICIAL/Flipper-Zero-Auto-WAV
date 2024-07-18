# Flipper-Zero-Auto-WAV
Automatically converts mp3 audio files into the .wav format with all the fancy requirements, which are 8k-bit with 48000Hz sampling rate, stereo audio

## Requirements:
1. FFmpeg installed + added to your Windows Environment Variables directory
2. Pydub module
3. Tkinter module
4. OS Module
5. Sys Module

Most of these modules should have already came pre-installed, but just in case they somehow weren't, it will be listed here.

## Tutorial
1. Get your mp3 audio file ready, recommended to have it in the same directory as the exe.
2. Drag the mp3 file onto the exe, and wait for the conversion to happen. CMD prompts will flash, do not worry--those are the Python scripts running.
3. If an error warning pops up, it means your audio file is not supported or something went wrong.
4. If successful, the final .wav file will be outputted in the same directory as the exe file.
5. Flash the new .wav file onto the Flipper's SSD card into the wav_player folder. (Recommended to directly do it instead of through qFlipper.)
