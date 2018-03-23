from __future__ import print_function

from pandas import DataFrame

from .magrittr import import_methods


import_methods(obj=DataFrame(), namespace=globals(), strict=True)


if __name__=='__main__':
    import numpy as np
    df = DataFrame(np.arange(9).reshape((3,3)), columns=list('abc'))
    print('>>> df')
    print(df)
    print(">>> df >> head(2)")
    print(df >> head(2))
    print(">>> df >> set_index('c')")
    print(df >> set_index('c'))
    print(">>> df >> set_index('c') >> stack()")
    print(df >> set_index('c') >> stack())
    print("\nDataFrame and Series share a lot of methods and by default we "
          "check the types as this can catch errors early and give more "
          " informative error messages.\n")
    print(">>> df >> set_index('c') >> stack() >> head(3)")
    try:
        print(df >> set_index('c') >> stack() >> head(3))
    except Exception as ex:
        print(ex)
    print("\nHowever this can be turned off and we can use duck-typing "
          "instead.\n")
    print(">>> import_methods(obj=DataFrame(), namespace=globals(), "
          "strict=False)")
    import_methods(obj=DataFrame(), namespace=globals(), strict=False)
    print(">>> df >> set_index('c') >> stack() >> head(3)")
    print(df >> set_index('c') >> stack() >> head(3))
