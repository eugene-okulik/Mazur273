# классный подкол, что операция с отрицательным числом была в конце
# и до нее просто не доходило, если писать декоратор в той же последовательности


num1, num2 = map(int, input('введи 2 числа: ').split())


def my_rules(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        return func(first, second, operation)
    return wrapper



@my_rules
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(num1, num2))
