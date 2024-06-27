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
### forecast
- [3 ETT datasets](https://github.com/zhouhaoyi/ETDataset) should be placed at `datasets/forecast/ETTh1.csv`, `datasets/forecast/ETTh2.csv` and `datasets/forecast/ETTm1.csv`.
- [Weather](https://archive.ics.uci.edu/dataset/381/beijing+pm2+5+data)should be placed at `datasets/forecast/Weather.csv`.
- [Airquality](https://archive.ics.uci.edu/dataset/360/air+quality)should be placed at `datasets/forecast/Airquality.csv`.
### classification
- [128UCRdatasets](https://www.cs.ucr.edu/~eamonn/time_series_data_2018) should be put into `datasets/UCR/` so that each data file can be located by `datasets/UCR/<dataset_name>/<dataset_name>_*.csv`.
Such as [Chinatown](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/Chinatown), [ItalyPowerDemand](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/ItalyPowerDemand), [RacketSports](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/RacketSports), [ArrowHead](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/ArrowHead), [SharePriceIncrease](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/SharePriceIncrease).
### anomaly
- [3 ETT datasets](https://github.com/zhouhaoyi/ETDataset) should be placed at datasets/forecast/ETTh1.csv, datasets/forecast/ETTh2.csv and datasets/forecast/ETTm1.csv.
## Usage
To train and evaluate TSG2L on a dataset, run the following command:
```bash
python train_forecast.py --dataset <dataset_name>  --run_name <run_name> --loader <loader> --gpu <gpu> 
```
**Scripts:** The scripts for reproduction are provided in scripts/ folder.
