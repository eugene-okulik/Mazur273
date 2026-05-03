import random


def how_much():
    salary = int(input('На какую ЗП рассчитываете? '))
    bonus = random.choice([True, False])
    if bonus:
        final_salary = salary + random.randrange(0, salary)
    else:
        final_salary = salary
    print(f"{salary}, {bonus} - '${final_salary}'")


how_much()
