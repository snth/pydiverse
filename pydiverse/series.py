from __future__ import print_function

from pandas import Series

from .magrittr import import_methods


import_methods(obj=Series(), namespace=globals(), strict=True)


if __name__=='__main__':
    import numpy as np
    s = Series(np.arange(5), index=list('abcde'))
    print('>>> s')
    print(s)
    print(">>> s >> head(2)")
    print(s >> head(2))
    print(">>> s >> reset_index()")
    print(s >> reset_index())
    print("\nDataFrame and Series share a lot of methods and by default we "
          "check the types as this can catch errors early and give more "
          " informative error messages.\n")
    print(">>> s >> reset_index() >> head(3)")
    try:
        print(s >> reset_index() >> head(3))
    except Exception as ex:
        print(ex)
    print("\nHowever this can be turned off and we can use duck-typing "
          "instead.\n")
    print(">>> import_methods(obj=Series(), namespace=globals(), "
          "strict=False)")
    import_methods(obj=Series(), namespace=globals(), strict=False)
    print(">>> s >> reset_index() >> head(3)")
    print(s >> reset_index() >> head(3))
