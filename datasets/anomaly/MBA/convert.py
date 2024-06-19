import numpy as np
import pandas as pd

# 读取.npy文件
labels = np.load('labels.npy')
test = np.load('test.npy')
train = np.load('train.npy')

# 转换为pandas DataFrame
labels_df = pd.DataFrame(labels)
test_df = pd.DataFrame(test)
train_df = pd.DataFrame(train)

# 将DataFrame保存为.csv文件
labels_df.to_csv('labels.csv', index=False)
test_df.to_csv('test.csv', index=False)
train_df.to_csv('train.csv', index=False)
