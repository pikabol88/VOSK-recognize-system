import sys
import os
#требует установки
#pip install librosa
#LibROSA - это пакет Python для анализа музыки и аудио.
import librosa
from scipy.io import wavfile

"""
Изменяет частоту дискретизации

Принимат: путь к файлу, требуемую частоту
"""
def reset_sample(path:str, new_sample:int):
	date, sample = librosa.load(path,new_sample) 
	#os.remove(path)
	new_path = path.split("/")
	path = path.replace(new_path[-1],'')
	#сохраняет с тем же названием, добавляя новую частоту
	path = path + str(new_sample)+new_path[-1]
	date = wavfile.write(path, sample,date)
