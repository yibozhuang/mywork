class Meta(type):
    def __new__(cls, name, bases, dicts):
        x = super().__new__(cls, name, bases, dicts)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass
