from __future__ import print_function


class PartialAction:

    def __init__(self, func, type_=None):
        if not callable(func):
            raise TypeError(func)
        self.func = func
        self.type_ = type_

    def __call__(self, *args, **kwargs):
        def _action(obj):
            if self.type_ is not None and not isinstance(obj, self.type_):
                raise TypeError('Expected {}: received {}'
                                .format(self.type_, type(obj)))
            return self.func(obj, *args, **kwargs)
        return DataAction(_action)


class DataAction:

    def __init__(self, action):
        if not callable(action):
            raise ValueError(action)
        self.action = action

    def __call__(self, *callargs):
        if len(callargs)==0:
            return self.action()
        elif len(callargs)>1:
            raise NotImplementedError()
        input = callargs[0]
        if isinstance(input, self.__class__):
            return DataAction(lambda x: self.action(input.action(x)))
        elif callable(input):
            return DataAction(lambda *args, **kwargs: 
                              self.action(input(*args, **kwargs)))
        else:
            return self.action(input)

    def __rshift__(self, right):
        if isinstance(right, DataAction):
            return right(self)
        elif right is None:
            return self.action()
        else:
            return DataAction(right)(self)

    def __rrshift__(self, left):
        if callable(left):
            return self(left)
        else:
            return self(left)


if __name__=='__main__':
    print('first')
    print(5 >> DataAction(lambda x: 2*x) >> DataAction(lambda x: x+1))
    print('second')
    print(range(5) >> DataAction(lambda x: [5*i for i in x]))
