import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# 仮想的な経済指標データを生成（本来は実際のデータを読み込む）
np.random.seed(42)
data = np.random.randn(100).cumsum() + 100
dates = pd.date_range("2000-01-01", periods=100, freq="Q")
ts = pd.Series(data, index=dates)

# 自己相関と偏自己相関のプロット
plot_acf(ts)
plot_pacf(ts)
plt.show()

# ARIMAモデルのフィッティング
# p: 自己回帰の次数, d: 差分の次数, q: 移動平均の次数
model = ARIMA(ts, order=(2, 1, 2))
results = model.fit()

# 予測
preds = results.predict(start=len(ts), end=len(ts) + 11, typ="levels")

# 結果のプロット
plt.figure(figsize=(10, 5))
plt.plot(ts, label="Observed")
plt.plot(preds, label="Forecast", linestyle="--")
plt.legend()
plt.show()
