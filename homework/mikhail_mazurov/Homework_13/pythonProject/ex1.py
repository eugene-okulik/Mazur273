import os
import datetime


file_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
print(homework_path)
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file_path)
my_list = []


def read_file():
    with open(eugene_file_path) as eugene_file:
        # text = eugene_file.read()
        # text = text.encode('cp1251').decode('utf-8')
        # хотелось красоты, жпт нашел нужную кодировку и синтаксис для изменений. текст задания перед глазами, кайф
        # но получается что я работаю уже с других файлом, по идее противоречит условиям, поэтому дальше юзаю ваш файл
        # print(text)
        for line in eugene_file.readlines():
            my_list.append(line[3:29])
        return my_list


read_file()
my_list = [datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S.%f') for i in my_list]
data1, data2, data3 = my_list
now = datetime.datetime.now()
print(data1 + datetime.timedelta(days=7))
print(data2.strftime('%A'))
print((now - data3).days)
