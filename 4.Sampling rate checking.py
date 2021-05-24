from scipy.io.wavfile import read as read_wav
sampling_rate, data = read_wav( wav_file_name) 
print (sampling_rate)
