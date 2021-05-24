# loading all the audio and text file paths of a given directory
wav_files = glob.gob ( ‘C: \\wav_file_directory\\*.wav’ )
text_files = glob.glob ( ‘C: \\text_file_directory\\*.txt’ )
audio_path = [ ]
for file_path in wav_files :
      audio_path.append ( file_path )
df00[ “Speech” ] = audio_path
text_path = [ ]
for file_path in text_files :
      text_path.append ( file_path )
df01[“Text”] = text_path
