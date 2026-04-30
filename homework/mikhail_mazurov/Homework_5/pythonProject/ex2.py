dano1 = 'результат операции: 42'
dano2 = 'результат операции: 514'
dano3 = 'результат операции: 9'
res1 = int(dano1[dano1.index(':') + 2:])+10
res2 = int(dano2[dano2.index(':') + 2:])+10
res3 = int(dano3[dano3.index(':') + 2:])+10
print(res1)
print(res2)
print(res3)