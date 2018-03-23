from pandas import DataFrame

from .magrittr import PartialAction


for name in dir(DataFrame):
    try:
        attr = getattr(DataFrame, name)
        if not name.startswith('_') and callable(attr):
            globals()[name] = PartialAction(attr, type_=DataFrame)
    except Exception as ex:
        print(ex)


if __name__=='__main__':
    import numpy as np
    import pandas as pd
    df = pd.DataFrame(np.arange(9).reshape((3,3)), columns=list('abc'))
    print('df')
    print(df)
    print("df >> head(2)")
    print(df >> head(2))
    print("df >> set_index('c')")
    print(df >> set_index('c'))
