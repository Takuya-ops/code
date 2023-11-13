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

dw_statistic
