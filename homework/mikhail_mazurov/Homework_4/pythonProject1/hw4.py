my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': ['one', 'two', 'three', 'four', 'five'],
           'dict': {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять'}, 'set': {'1', '2', '3', '4', '5'}}
print(my_dict['tuple'][-1])
my_dict['list'].append(42)
my_dict['list'].pop(1)
# print(my_dict)  # проверка для себя что всё ок
my_dict['dict'][('i am a tuple',)] = (1, 2)
my_dict['dict'].pop('2')
# print(my_dict)  # проверка для себя что всё ок
my_dict['set'].add('шесть')
my_dict['set'].remove('шесть')  # да, мне приспичило найти как конкретный элемент удалить, поэтому pop не использовал
# print(my_dict)  # проверка для себя что всё ок
print(my_dict)
