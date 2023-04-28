# MP3 to WAV Converter
This is a Python script that can be used to convert MP3 audio files to WAV format. The script takes two arguments: the input folder containing the MP3 files and the output folder where the WAV files will be saved. The script uses the pydub library to perform the conversion.

Requirements
Python 3.x
pydub library (pip install pydub)

Usage
1. Install the pydub library by running the following command in your terminal:
pip install pydub

2. Download or clone this repository to your local machine.

3. Open your terminal or command prompt and navigate to the downloaded directory.

4. Run the following command in your terminal or command prompt, replacing input_folder with the path to the folder containing the MP3 files and output_folder with the path to the folder where you want to save the converted WAV files:
python mp3_to_wav_converter.py input_folder output_folder

5. Wait for the script to complete. The converted WAV files will be saved in the specified output folder.

Note
The script only converts files with the .mp3 extension. Other file formats will be ignored.

The converted files will have the same name as the original files, but with the .wav extension. If a file with the same name already exists in the output folder, it will be overwritten.
