import os
import argparse
from pydub import AudioSegment

# Define command-line arguments
parser = argparse.ArgumentParser(description='Convert MP3 files to WAV')
parser.add_argument('input_folder', help='Path to the folder containing MP3 files')
parser.add_argument('output_folder', help='Path to the folder where WAV files will be saved')

# Parse command-line arguments
args = parser.parse_args()

# Convert each MP3 file to WAV format and save in output folder
for file_name in os.listdir(args.input_folder):
    if file_name.endswith('.mp3'):
        mp3_path = os.path.join(args.input_folder, file_name)
        wav_path = os.path.join(args.output_folder, os.path.splitext(file_name)[0] + '.wav')
        AudioSegment.from_file(mp3_path).export(wav_path, format='wav')
