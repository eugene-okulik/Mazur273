PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# my_list = PRICE_LIST.split()
# list_of_subj = list(filter(lambda x: my_list.index(x) % 2 == 0, my_list))
# list_of_price = list(filter(lambda x: my_list.index(x) % 2 == 1, my_list))
# list_of_price2 = list(map(lambda x: int(x[:-1]), list_of_price))
# new_dict = dict(zip(list_of_subj, list_of_price2))

new_dict = dict(zip(PRICE_LIST.split()[::2], map(lambda x: int(x[:-1]), PRICE_LIST.split()[1::2])))

# print(list_of_subj)
# print(list_of_price)
# print(list_of_price2)
print(new_dict)

