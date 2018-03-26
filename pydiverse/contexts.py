from __future__ import print_function
import contextlib



@contextlib.contextmanager
def bound_obj_and_stored_globals(obj, globals_):

    def safe_keys(keys, exclusions=['In', 'Out']):
        return [k for k in keys if not k.startswith('_') and k not in exclusions]

    # store existing global variables
    stored_globals = {}
    for k in safe_keys(globals_):
        stored_globals[k] = globals_[k]
        del globals_[k]
    # import the variables from obj
    for k in obj:
        globals_[k]= obj[k]
    yield stored_globals
    # update obj and remove the temporary global variables
    for k in safe_keys(globals_):
        obj[k] = globals_[k]
        del globals_[k]
    # restore the stored global variables
    for k in stored_globals:
        globals_[k] = stored_globals[k]
    return


if __name__=='__main__':
    d = dict(a=1, b=2, c=3)
    print(d)
    print([k for k in globals().keys() if not k.startswith('_')])
    with bound_obj_and_stored_globals(d, globals()):
        # print(globals().keys())
        # print([k for k in globals().keys() if not k.startswith('_')])
        d = 4
        e = b + c
    print([k for k in globals().keys() if not k.startswith('_')])
    print(d)
