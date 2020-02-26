import abc


class Double(metaclass=abc.ABCMeta):
    pass


@Double.register
class Double64:
    pass
