python -u train_forecast.py     --dataset ETTm2  --size_cent  576   --size_1 576  --epoch  3   --epoch_1  9  --gru_dime   20  --a_3  400  --c  60  --pred_len  80  --p_recon 1  --p  0.3 --multi  20 --count  3  --port  6 --run_name  forecast_csv --loader forecast_csv  --gpu 0  --seed 42  --max-threads  8