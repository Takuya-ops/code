import numpy as np
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson

# サンプルデータを生成
np.random.seed(42)
n = 100  # データ点の数
X = np.linspace(0, 10, n)
Y = 2.0 + 1.5 * X + np.random.normal(0, 2, n)  # 線形関係にランダムノイズを加える

# 線形回帰モデルのフィット
X = sm.add_constant(X)  # 定数項（切片)を追加
model = sm.OLS(Y, X).fit()

# ダービン・ワトソン検定の実行
dw_statistic = durbin_watson(model.resid)

print(dw_statistic)


# スクラッチ実装の場合
import numpy as np
from sklearn.linear_model import LinearRegression

# サンプルデータの生成
np.random.seed(42)
n = 100
X = np.linspace(0, 10, n).reshape(-1, 1)
Y = 2.0 + 1.5 * X.flatten() + np.random.normal(0, 2, n)

# 線形回帰モデルのフィット
model = LinearRegression().fit(X, Y)
Y_pred = model.predict(X)
residuals = Y - Y_pred

# ダービン・ワトソン統計量の計算
dw_numerator = np.sum(np.diff(residuals) ** 2)
dw_denominator = np.sum(residuals**2)
dw_statistic = dw_numerator / dw_denominator

print(dw_statistic)
