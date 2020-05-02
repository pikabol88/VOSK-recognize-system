#!/usr/bin/python3

#from vosk import Model, KaldiRecognizer
import sys
#import os
import wave
from convert import conv_mp3_to_wav
from recognize import recognize 
from infile import save_in_file
from downsample import reset_sample

audio = sys.argv[1]
audio = conv_mp3_to_wav(str(audio))
result = recognize(str(audio))

path = audio 
out = path.split('/')[-1]
out = out.replace('wav','txt')
out = "text/" + out

save_in_file(result,out)
sample_list = [8000, 16000, 32000, 48000]
wf = wave.open(path, "rb")
sample = wf.getframerate()
wf.close()
tmp = sample
new_sample = 0
if sample not in sample_list:
	for i in sample_list:
		if abs(sample-i) < tmp:
			new_sample = i
			tmp = abs(sample-i)
	#добавить поиск размера
	reset_sample(path,new_sample)
	#wf = wave.open(path, "rb")
	#sample = wf.getframerate()
	#print(sample)
