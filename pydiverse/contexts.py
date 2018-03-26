from __future__ import print_function


class BoundObjAndStoredGlobals(object):

    def __init__(self, obj, globals_):
        self.obj = obj
        self.globals_ = globals_

    @staticmethod
    def safe_keys(keys, exclusions=['In', 'Out']):
        return [k for k in keys if not k.startswith('_') and k not in
                exclusions]

    def __enter__(self):
        # store existing global variables
        self.stored_globals = {}
        for k in self.safe_keys(self.globals_):
            self.stored_globals[k] = self.globals_[k]
            del self.globals_[k]
        # import the variables from obj
        for k in self.obj:
            self.globals_[k]= self.obj[k]
        return self.stored_globals

    def __exit__(self, *args):
        # update obj and remove the temporary global variables
        for k in self.safe_keys(self.globals_):
            self.obj[k] = self.globals_[k]
            del self.globals_[k]
        # restore the stored global variables
        for k in self.stored_globals:
            self.globals_[k] = self.stored_globals[k]
        return

if __name__=='__main__':
    d = dict(a=1, b=2, c=3)
    print(d)
    print([k for k in globals().keys() if not k.startswith('_')])
    with BoundObjAndStoredGlobals(d, globals()):
        # print(globals().keys())
        # print([k for k in globals().keys() if not k.startswith('_')])
        d = 4
        e = b + c
    print([k for k in globals().keys() if not k.startswith('_')])
    print(d)
