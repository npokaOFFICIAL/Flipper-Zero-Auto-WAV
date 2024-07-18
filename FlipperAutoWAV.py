import os
import sys
from pydub import AudioSegment
import tkinter as tk
from tkinter import messagebox

def convert_to_wav(input_file, output_file, channels=1, sample_rate=8000):
    try:
        audio = AudioSegment.from_file(input_file)
        audio = audio.set_frame_rate(sample_rate)
        audio = audio.set_sample_width(1)
        audio = audio.set_channels(channels)
        audio.export(output_file, format='wav', codec='pcm_u8')
    except Exception as e:
        show_error_popup(f"An error occurred during conversion: {str(e)}")

def show_error_popup(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", message)
    root.destroy()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        show_error_popup("Please provide the path to the audio file.")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + ".wav"
    convert_to_wav(input_file, output_file, channels=2, sample_rate=48000)