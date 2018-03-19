from functools import partial

import pandas as pd


def arrange(*args, **kwargs):
    return partial(pd.DataFrame.sort_values, by=list(args), **kwargs)


def filter(*args, **kwargs):
    return partial(pd.DataFrame.query, expr='&'.join(map('({})'.format, args)),
                   **kwargs)


def group_by(*args, **kwargs):
    return partial(pd.DataFrame.groupby, by=list(args), **kwargs)


def mutate(*args, **kwargs):
    kwargs['inplace'] = kwargs.get('inplace', False)

    def _mutate(df):
        for expr in args:
            result = df.eval(expr=expr, **kwargs)
            if not kwargs['inplace'] and isinstance(result, pd.DataFrame):
                df = result
        if not kwargs['inplace']:
            return df
    return _mutate
    # return partial(_mutate, expressions=args, kwds=kwargs)


def select(*args):
    return partial(pd.DataFrame.__getitem__, key=list(args))


def summarise(*args, **kwargs):

    def _summarise(obj):
        return obj.aggregate(*args, **kwargs)

    return _summarise
