from __future__ import print_function


class BoundObjAndStoredGlobals(object):

    def __init__(self, obj, globals_, exclusions={'In', 'Out'}):
        self.obj = obj
        self.globals_ = globals_
        self.exclusions = exclusions
        self.exclusions.update(k for k in globals_ if k.startswith('_'))

    def safe_keys(self):
        return [k for k in self.globals_ if k not in self.exclusions]

    def __enter__(self):
        # store existing global variables
        self.stored_globals = {}
        for _k in self.safe_keys():
            self.stored_globals[_k] = self.globals_[_k]
            del self.globals_[_k]
        # import the variables from obj
        for _k in self.obj:
            self.globals_[_k]= self.obj[_k]
        return self

    def __exit__(self, *args):
        # update obj and remove the temporary global variables
        for _k in self.safe_keys():
            if self.globals_[_k] is not self:
                self.obj[_k] = self.globals_[_k]
            del self.globals_[_k]
        # restore the stored global variables
        for _k in self.stored_globals:
            self.globals_[_k] = self.stored_globals[_k]
        return

    def __getattr__(self, attr):
        return getattr(self.stored_globals, attr)

if __name__=='__main__':
    d = dict(a=1, b=2, c=3)
    print([k for k in globals().keys() if not k.startswith('_')])
    print(d)
    with BoundObjAndStoredGlobals(d, globals()) as context:
        print(context.keys())
        print([k for k in globals().keys() if not k.startswith('_')])
        del k
        d = 4                   # noqa
        e = b + c               # noqa
    print(d)
    print([k for k in globals().keys() if not k.startswith('_')])
