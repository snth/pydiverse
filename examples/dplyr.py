# flake8: noqa
import numpy as np
import pandas as pd

from pydiverse import *

df = pd.DataFrame(np.arange(12).reshape(4,3), columns=list('abc'))

# arrange
(do
 >> df
 << print('Initial DataFrame:')
 >> print
 >> mutate('d = c % 2')
 << print('After mutate:')
 >> print 
 >> arrange('d', 'c', desc='c')
 << print('After arrange:')
 >> print
 >> group_by('d')
 >> summarise('sum')
 << print('After group_by("d") >> summarise("sum"):')
 >> print
 >> done
 )
