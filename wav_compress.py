import sys
import wave
import audioop
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a .wav file to compress", filetypes=[("WAV files", "*.wav")])
    return file_path

def compress_wav_file(input_file, output_file, compression_ratio):
    with wave.open(input_file, 'rb') as wav_in:
        params = wav_in.getparams()
        nchannels, sampwidth, framerate, nframes = params[:4]

        audio_data = wav_in.readframes(nframes)
        new_framerate = int(framerate * compression_ratio)
        audio_data_compressed, _ = audioop.ratecv(audio_data, sampwidth, nchannels, framerate, new_framerate, None)

        with wave.open(output_file, 'wb') as wav_out:
            wav_out.setparams(params)
            wav_out.setframerate(new_framerate)
            wav_out.writeframes(audio_data_compressed)

        print(f"Compressed file saved as {output_file}")

if __name__ == "__main__":
    input_file = select_file()

    if not input_file:
        print("No file selected.")
    else:
        output_file = input_file.replace(".wav", "_compressed.wav")
        compression_ratio = 0.6
        compress_wav_file(input_file, output_file, compression_ratio)
