dano1 = 'результат операции: 42'
dano2 = 'результат операции: 514'
dano3 = 'результат операции программы: 9'

# так как индексом я уже делал, попробую split


def plus10(my_string: str):
    my_list = my_string.split()  # сработало то о чем писал в ex2, метод split был в подсказках
    print(int(my_list[-1]) + 10)


plus10(dano1)
plus10(dano2)
plus10(dano3)
