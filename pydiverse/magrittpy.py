from __future__ import print_function

DONE = object()


class Pipe:

    def __init__(self, state=None):
        self.state = state

    def __rshift__(self, operand):
        print(self.state)
        if self.state is None:
            self.state = operand
        elif callable(operand):
            result = operand(self.state)
            if result is not None:
                self.state = result
        elif operand is DONE:
            return self.state
        else:
            raise NotImplementedError((type(self.state), type(operand)))
        return self

    __or__ = __rshift__

do = Pipe()
done = DONE

if __name__=='__main__':
    print('first')
    print(Pipe(5) >> (lambda x: 2*x) >> (lambda x: x+1) >> done)
    print('second')
    (do
     >> range(5)
     >> (lambda x: [5*i for i in x])
     >> done
     )  # noqa: W503
    print('third')
    do = Pipe()
    (do
     | range(5)
     | (lambda x: [5*i for i in x])
     | done
     )
