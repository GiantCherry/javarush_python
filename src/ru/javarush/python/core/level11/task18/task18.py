# Зона видимости переменной.

# Исправьте код, чтобы последний print выводил исключение.

def bar(i):
    if i == 1:
        raise KeyError(1)
    if i == 2:
        raise ValueError(2)

def bad():
    exception = None
    try:
        bar(1)
    except KeyError as e:
        exception = e
        print('key error')
    except ValueError as e:
        exception = e
        print('value error')
    print(exception)  # This should raise an exception because e is not defined in this scope

bad()
