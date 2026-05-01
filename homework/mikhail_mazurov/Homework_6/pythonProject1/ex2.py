my_range = []
for j in range(1, 101):
    if j % 3 == 0 and j % 5 == 0:
        my_range.append('FuzzBuzz')
    elif j % 3 == 0:
        my_range.append('Fuzz')
    elif j % 5 == 0:
        my_range.append('Buzz')
    else:
        my_range.append(j)
for i in my_range:
    print(i)
