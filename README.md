# VOSK-recognize-system
Система распознования русской речи, основанная на Kaldi.

Формат распознаваемого файла - PCM 16кГц 16бит 1канал.

# Установка для работы Python из Pypi
Можно установить "Воск" с помощью pip. 
Для начала убедитесь, что используются достаточно новые версии pip и Python:

    Python версия >= 3.5
    pip версия >= 19.0

Обновите Python и Pip если нужно, а затем установите "Воск" такой командой :

    pip3 install vosk 

# Запуск примера (Linux) 

Выполните следующие команды:

    git clone https://github.com/kaldi-asr/kaldi

    cd VOSK/example
    wget http://alphacephei.com/kaldi/models/vosk-model-ru-0.10.zip
    unzip vosk-model-ru-0.10.zip
    mv vosk-model-ru-0.10.zip model
    python3 test.py mp3/test.mp3 

