python -u train_forecast.py     --dataset ETTh1  --size_cent  570   --size_1 570  --epoch  9    --epoch_1 8  --gru_dime   50 --a_3 500 --c 48  --pred_len 200  --p_recon 1
--p 0.5 --multi 40 --count 4  --port 6 --run_name forecast_csv --loader forecast_csv 
--gpu 0  --seed 42  --max-threads  8