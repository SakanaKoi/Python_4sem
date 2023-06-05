def get_inheritance(cls):
    return ' -> '.join([c.__name__ for c in cls.mro()])

print(get_inheritance(OSError))