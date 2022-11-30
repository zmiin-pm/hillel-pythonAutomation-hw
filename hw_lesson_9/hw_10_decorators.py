def call_times(file_name):
    def decorator(func):
        def wrapper():
            wrapper.count += 1
            with open(file_name, 'w') as f:
                f.write(f'{func.__name__} была вызвана {wrapper.count} раз(а).\n')
            return func()

        wrapper.count = 0
        return wrapper

    return decorator


@call_times('foo.txt')
def foo():
    pass


@call_times('boo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
