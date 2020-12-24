### 说明
这是2020年课程《机器学习》的结课论文附属的代码文件。

主要采用CNN预测股价

main.py ：模型的主要所有代码
get_data.py : 获取股票数据

### 环境
TensorFlow==2.1.0
python==3.6
tushare

### 运行过程
1 运行get_data.py 获取到贵州茅台的股价数据，保存到SH600519_2020_12_20.csv

2 运行main.py 训练并测试模型
