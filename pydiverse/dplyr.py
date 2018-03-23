from functools import partial

from pandas import DataFrame

from .magrittr import PartialAction, DataAction


def arrange(*args, **kwargs):
    desc = kwargs.pop('desc', [])
    if isinstance(desc, bool):
        desc = list(args) if desc else []
    elif isinstance(desc, str):
        desc = [desc]
    ascending = [not(c in desc) for c in args]
    return DataAction(partial(DataFrame.sort_values, by=list(args), 
                              ascending=ascending, **kwargs))


def filter(*args, **kwargs):
    return DataAction(partial(DataFrame.query,
                              expr='&'.join(map('({})'.format, args)),
                              **kwargs))


def group_by(*args, **kwargs):
    return DataAction(partial(DataFrame.groupby, by=list(args), **kwargs))


def mutate(*args, **kwargs):
    kwargs['inplace'] = kwargs.get('inplace', False)

    def _mutate(df):
        for expr in args:
            result = df.eval(expr=expr, **kwargs)
            if not kwargs['inplace'] and isinstance(result, DataFrame):
                df = result
        if not kwargs['inplace']:
            return df
    return DataAction(_mutate)
    # return partial(_mutate, expressions=args, kwds=kwargs)


def select(*args):
    return DataAction(partial(DataFrame.__getitem__, key=list(args)))


def summarise(*args, **kwargs):

    def _summarise(obj):
        return obj.aggregate(*args, **kwargs)

    return DataAction(_summarise)


if __name__=='__main__':
    import numpy as np
    import pandas as pd
    df = pd.DataFrame(np.arange(9).reshape((3,3)), columns=list('abc'))
    print('df')
    print(df)
    print("df >> arrange('a', desc=True)")
    print(df >> arrange('a', desc=True))
    print("df >> mutate('d=a%2')")
    print(df >> mutate('d=a%2'))
    print("df >> mutate('d=a%2') >> group_by('d') >> summarise('sum')")
    print(df >> mutate('d=a%2') >> group_by('d') >> summarise('sum'))
