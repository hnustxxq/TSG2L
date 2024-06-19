import numpy as np
import pandas as pd
import os

# 假设我们在当前目录下工作
directory = 'D:\实验模型\model_1_测试_矩阵乘法\processed\SMAP'  # 将这里替换为包含.npy文件的目录的路径

# 遍历目录下的所有文件
for file in os.listdir(directory):
    if file.endswith("_labels.npy") or file.endswith("_test.npy") or file.endswith("_train.npy"):
        # 构建完整的文件路径
        file_path = os.path.join(directory, file)

        # 读取.npy文件
        data = np.load(file_path)

        # 将NumPy数组转换为pandas DataFrame
        df = pd.DataFrame(data)

        # 创建新的文件名并替换后缀为.csv
        csv_file = file.replace('.npy', '.csv')

        # 将DataFrame保存为.csv文件
        df.to_csv(os.path.join(directory, csv_file), index=False)

        os.remove(file_path)

        print(f"{file} has been converted to {csv_file}.")
