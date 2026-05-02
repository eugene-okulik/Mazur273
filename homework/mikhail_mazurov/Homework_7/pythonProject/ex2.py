words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def multipl_key(my_dict):
    # print(my_dict.items())
    for key, degree in my_dict.items():
        print(key * degree)


multipl_key(words)
# стросил у жпт, оказывается можно указывать тип параметра и тогда нотационные методы типа .items будут подсказываться
# проверю в след.задании
