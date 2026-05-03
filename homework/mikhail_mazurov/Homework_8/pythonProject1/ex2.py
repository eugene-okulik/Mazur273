
goals = [5, 200, 1000, 10000]  # заменил 100к на 10к, т.к была ошибка "Exceeds the limit
                               # (4300 digits) for integer string conversion;"
res = []


def fibonachi_numb():
    numb1 = 0
    numb2 = 1
    count = 1
    while True:
        yield numb1
        numb1, numb2 = numb2, numb1 + numb2
        count += 1


count = 1
for number in fibonachi_numb():
    if count in goals:
        res.append(number)
    if len(res) == len(goals):
        break
    count += 1

print(res)
