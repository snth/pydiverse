from __future__ import print_function

EMPTY = object()
DONE = object()


class Pipe:

    def __init__(self, state=EMPTY):
        self.state = state

    def __rshift__(self, operand):
        try:
            if self.state is EMPTY:
                self.state = operand
            elif callable(operand):
                result = operand(self.state)
                if result is not None:
                    self.state = result
            elif operand is DONE:
                state, self.state = self.state, EMPTY
                return state
            else:
                # FIXME: Display warning about forgotten 'done'
                raise NotImplementedError((type(self.state), type(operand)))
        except:
            # Ensure `do` instance is reset properly on errors
            self.state = EMPTY
            raise
        return self

    def __lshift__(self, operand):
        "Like >> but doesn't update state so used for its side-effects"
        try:
            if self.state is EMPTY:
                self.state = operand
            elif callable(operand):
                result = operand(self.state)    # noqa:
            elif operand is DONE:
                state, self.state = self.state, EMPTY
                return state
        except:
            # Ensure `do` instance is reset properly on errors
            self.state = EMPTY
            raise
        return self

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
