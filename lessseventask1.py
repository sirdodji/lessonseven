def split_string(func):
    def wrapper():
        s = func().split()
        print(s)
    return wrapper

@split_string
def stroka():
    new_string = str(input("введите слова: "))
    print(new_string)
    return new_string

stroka()