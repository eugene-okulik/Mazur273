temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


hot_days_filter = filter(lambda x: x > 28, temperatures)
new_list_hot_days_filter = list(hot_days_filter)


# print(new_list_hot_days_filter)
print(max(new_list_hot_days_filter))
print(min(new_list_hot_days_filter))
print(round((sum(new_list_hot_days_filter) / len(new_list_hot_days_filter)), 3))
