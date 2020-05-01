#!/usr/bin/python3

from vosk import Model, KaldiRecognizer
#Модуль os предоставляет множество функций для работы с операционной системой
import os
#Модуль обеспечивает удобный интерфейс для формата WAV звука
import wave
#Система параметризации структуры данных, написанная для встраивания контекста в объекты JSON
import json

"""
Модуль, осуществляющий перевод аудиофрагмента в текст, посредством использования vosk-api, построенной на системе распознавания kaldi
"""
"""
Принимает: строку - путь к файлу ФОРМАТА WAV
Возвращает: результат перевода в JSON формате
"""
def recognize(str_wav:str):
	if not os.path.exists("model"):
	    print ("Please download the model (vosk-model-ru-0.10.zip) from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
	    exit (1)
	wf = wave.open(str_wav, "rb")
	if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
	#getnchannels() -> Возвращает количество аудиоканалов ( 1для моно, 2для стерео)
	#getsampwidth() -> Возвращает ширину образца в байтах
	#getcomptype() -> Возвращает тип сжатия ( 'NONE'это единственный поддерживаемый тип)
	#то есть все эти проверки на то, что нам на самом деле подсунули нужный формат
	    print ("Audio file must be WAV format mono PCM.")
	    print(wf.getnchannels())
	    print(wf.getsampwidth())
	    print(wf.getcomptype())
	    exit (1)
	
	
	#список для объединения результатов
	result = list()
	#Обученная модель для русского языка 
	model = Model("model")
	#wf.getframerate()->Возвращает частоту дискретизации.
	rec = KaldiRecognizer(model, wf.getframerate())	
	while True:
		data = wf.readframes(1000)
		if len(data) == 0:
			break
		if rec.AcceptWaveform(data):
			#вытаскиваю результат из строки в JSON формате
			jsonData = json.loads(rec.Result())
			result.append(jsonData)
	jsonData = json.loads(rec.FinalResult())
	#Проверка на пустоту
	if 'result' in jsonData:
		result.append(jsonData)
	
	#перевожу обратно в JSON формат
	final = json.dumps(result,ensure_ascii=False)
	
	return final
	
