import sys
import os
import librosa
from scipy.io import wavfile


def reset_sample(path:str, new_sample:int):
	date, sample = librosa.load(path,new_sample) 
	#os.remove(path)
	new_path = path.split("/")
	path = path.replace(new_path[-1],'')
	path = path + str(new_sample)+new_path[-1]
	date = wavfile.write(path, sample,date)
