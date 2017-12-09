#coding:utf-8
# import pandas as pd
# import numpy as np
# p1 = pd.Panel(np.arange(27).reshape((3,3,3)))
# print(p1)
# print(p1.values)
#coding:utf-8
import numpy as np
import pandas as pd
from pandas_datareader import *
from pandas import Series, DataFrame, Index, Panel

# da= get_data_yahoo('AAPL')
# print(da)
data =dict((stk, get_data_yahoo(stk, '1/1/2016', '1/15/2016')) for stk in ['AAPL', 'GOOG', 'BIDU', 'MSFT'])
print(data)
pdata = Panel(data)
print(pdata)
# pdata = pdata.swapaxes('items', 'minor')
print(pdata)
#访问顺序：# Item -> Major -> Minor

print(pdata['AAPL'])
print(pdata[:, '1/5/2016', :])
print(pdata['AAPL', '1/6/2016', :])


#Panel与DataFrame相互转换
stacked = pdata.ix[:, '1/7/2016':, :].to_frame()
print(stacked)
print(stacked.to_panel())