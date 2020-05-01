#!/usr/bin/python3

#from vosk import Model, KaldiRecognizer
import sys
#import os
#import wave
from convert import conv_mp3_to_wav
from recognize import recognize 
from infile import save_in_file

audio = sys.argv[1]
audio = conv_mp3_to_wav(str(audio))
result = recognize(str(audio))

path = audio 
out = path.split('/')[-1]
out = out.replace('wav','txt')
out = "text/" + out

save_in_file(result,out)
