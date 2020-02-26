Foo = type('Foo', (), {})
x = Foo()


class Bar:
    pass


y = Bar()


Kick = type('Kick', (Foo,), dict(attr=100))


class Nick(Foo):
    attr = 100


Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': lambda x: x.attr
    }
)


class Foo:
    attr = 100

    def attr_val(self):
        return self.attr


def f(obj):
    print('attr =', obj.attr)


Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': f
    }
)


class Foo:
    attr = 100
    attr_val = f
