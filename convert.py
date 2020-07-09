#!/usr/bin/python3
# Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python 
import sys
#Модуль os предоставляет множество функций для работы с операционной системой
import os
#Модуль для оперирования с аудио
import pydub
#Модуль обеспечивает удобный интерфейс для формата WAV звука
import wave

#vosk работает только с форматом wav => было принято решение переводить входные mp3.

"""
Модуль отвечает за конвертацию аудиофайла mp3 формата в wav, с сохранением wav файла.
Так как наш распознаватель настроен на работу с моно mp3, добавила конвертацию из стерео в моно.
"""
"""
Принимает: строку - путь к исходному mp3 файл
Возвращает: строку - путь к конвертированному wav файлу
"""

def conv_mp3_to_wav(mp3:str):
	str_mp3 = mp3
	str_wav = str_mp3.replace('mp3','wav')
	sound = pydub.AudioSegment.from_mp3(str_mp3)
	#sound.export(str_wav, format="wav")
	wav = sound.export(str_wav, format="wav")
	
	#открывает файл в формате wav
	wf = wave.open(str_wav, "rb")
	
	#перевод из стерео в моно
	if wf.getnchannels() != 1:
	   wf.close()
	   sound_new = pydub.AudioSegment.from_wav(str_wav)
	   sound_new = sound_new.set_channels(1)
	   os.remove(str_wav)
	   sound_new.export(str_wav, format="wav")  
	   wf = wave.open(str_wav, "rb")
	   
	wf.close()
	return str_wav

"""
!!! Сохранение wav файла может нам и не пригодиться.
Но я не нашла способ  обойти данное действие, так как WAVE и PYDUP работаю с совершенно разными объектами, которые они создают самостоятельно, принимая путь файла 
=>
Если сохранение файла будет затратным и не нужным, эту проблему легко решить с помощью os.remove(str_wav)
"""
