# loading all the flac files of a given directory
file_paths = Path ( ‘C: \\wav_file_path’ ).glob(‘./*flac’)
for f_path in file_paths :
flac_tmp_speech_data = AudioSegment.from_file(f_path, f_path.suffix[1:] )
flac_tmp_speech_data.export(f_path.name.replace(f_path.suffix, “”) + “.wav”, format=”wav”)
os.remove(f_path)
