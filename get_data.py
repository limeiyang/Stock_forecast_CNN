import tushare as ts
import matplotlib.pyplot as plt

# 读取贵州茅台的日K量数据
df1 = ts.get_k_data('600519', ktype='D', start='2010-12-20', end='2020-12-20')

datapath1 = "./SH600519_2020_12_20.csv"
df1.to_csv(datapath1)
