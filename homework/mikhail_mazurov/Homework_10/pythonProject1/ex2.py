

def repeat_me(func):
    def wrapper(string, count):
        result = print(f'{string}\n' * count, )
        return result
    return wrapper


@repeat_me
def example(text):
    print(text)

example('print me', count=2)


# было время и желание повозиться, ниже необязательная часть задания но не уверен в результате


def repeat_me2(count):
    def second_level(func):
        def wrapper(string):
            for i in range(count):
                print(string)
        return wrapper
    return second_level


@repeat_me2(count=2)
def example(text):
    print(text)


example('print me')

