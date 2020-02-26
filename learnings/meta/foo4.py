class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


class X(metaclass=Meta):
    pass


class Y(metaclass=Meta):
    pass


class Base:
    attr = 100


class X2(Base):
    pass


class Y2(Base):
    pass


def decorator(cls):
    class NewClass(cls):
        attr = 100

    return NewClass


@decorator
class X3:
    pass


@decorator
class Y3:
    pass
