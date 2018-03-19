# flake8: noqa
import numpy as np
import pandas as pd

from pydiverse import *

df = pd.DataFrame(np.arange(12).reshape(4,3), columns=list('abc'))

# printing
(do
 >> df
 >> print
 >> done
 )

# arrange
(do
 >> df
 >> mutate('d = c % 2')
 >> arrange('d', 'c', desc='c')
 >> print
 >> done
 )


# group_by
(do
 >> df
 >> mutate('d = c % 2')
 >> group_by('d')
 >> summarise('sum')
 >> print
 >> done
 )
