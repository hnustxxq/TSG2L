# TSG2L
This repository contains the official implementation for the paper [Robust multivariate time series representation learning from global to local perspective]().

## Requirements
The recommended requirements for TSG2L are specified as follows:

- Python 3.7
- torch==1.12.0
- numpy==1.21.6
- pandas==1.0.1
- scikit-learn==0.24.2
- scipy==1.7.3
The dependencies can be installed by:
```bash
pip install -r requirements.txt
```
## Data 
The datasets can be obtained and put into datasets/ folder in the following way:
- [3 ETT datasets](https://github.com/zhouhaoyi/ETDataset) should be placed at datasets/ETTh1.csv, datasets/ETTh2.csv and datasets/ETTm1.csv.
- [Weather](https://archive.ics.uci.edu/dataset/381/beijing+pm2+5+data). should be placed at datasets/ETTh1.csv.
- [](). 
## Usage
To train and evaluate TSG2L on a dataset, run the following command:
```bash
python
```
#### Scripts: The scripts for reproduction are provided in scripts/ folder.
