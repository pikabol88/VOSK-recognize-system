import re

inaccuracy = 0.1

def load_file(file_name):
    '''
    Возвращает копию файла
    :param file_name:  str  -  имя файла
    :return:  str  -  содержимое файла
    '''
    file = open(file_name, "r")
    text = file.read()
    file.close()
    return text


def parse_words(text):
    '''
    Парсинг файла текста
    :param text:  str  -  копия файла с текстом
    :return:  list(list(str, list(float, float)))  - слово, интервал времени произношения
    '''
    real_num_pattern = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'
    word_pattern = r'/.*?/'
    words = re.findall(real_num_pattern + word_pattern + real_num_pattern, text)
    res_list = list()
    for i in words:
        times = [float(i) for i in re.findall(real_num_pattern, i)]
        word = re.findall(word_pattern, i)[0][1: -1]
        res_list.append([word, times])
    return res_list


def parse_time(times):
    '''
    Парсинг файла времени
    :param times:  str  -  копия текста из фалйа времени
    :return:  list(list(float, float))  -  готовая структура интервалов
    '''
    times = times.split(" speech\n")
    times = [i.split() for i in times]
    time_parsed = list()
    for interval in times:
        try:
            time_parsed.append([float(interval[0]), float(interval[1])])
        except IndexError:
            pass
    return time_parsed


def create_file(file_name, text_parsed, time_parsed):
    '''
    Функция создающая файл из распаршенных файлов времени и текста
    :param file_name:  str  -  имя итогового файла
    :param text_parsed:  list(list(str, list(float, float)))  -  разобранные слова с метками времени
    :param time_parsed:  list(list(float, float))  -  интервалы времени произноешния фраз
    :return:
    '''
    res_file = open(file_name, "w")

    interval_counter = -1
    words_counter = 0
    for i in time_parsed:
        interval_counter += 1

        string = "(Speaker 1) :"
        if interval_counter % 2 == 0:
            string = "(Speaker 0) :"

        if words_counter > len(text_parsed) or i[1] < text_parsed[words_counter][1][1]:
            continue

        string += " <" + str(text_parsed[words_counter][1][0]) + "> "
        while words_counter < len(text_parsed) and i[1] > text_parsed[words_counter][1][1]:
            string += " " + text_parsed[words_counter][0]
            words_counter += 1
        string += " <" + str(text_parsed[words_counter - 1][1][1]) + ">\n"
        res_file.write(string)

    res_file.close()


def merge(text_file, time_file):
    '''
    Функция создающая итоговый файл по результатам распознавания и диаризации
    :param text_file:  str  -  имя файла с текстом
    :param time_file:  str -  имя файла с таймкодами
    :return:  str  -  имя готового к анализу файла
    '''
    text_str = load_file(text_file)  # Сохранение текста
    times = load_file(time_file)  # Сохранение времени

    text_parsed = parse_words(text_str)  # Парсинг текста
    time_parsed = parse_time(times)  # Парсинг времени

    res_filename = 'res.txt'
    create_file(res_filename, text_parsed, time_parsed)  # Слияние в один файл
    return res_filename
