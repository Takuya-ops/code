import pymc3 as pm
import numpy as np

# 正規分布からのデータを生成する例
true_mean = 0
true_std = 1
observed_data = np.random.normal(true_mean, true_std, 100)

# モデルを定義
with pm.Model() as model:
    # 未知パラメータの事前分布
    mean = pm.Normal("mean", mu=0, sd=1)
    std = pm.HalfNormal("std", sd=1)

    # 観測データに対する尤度関数
    observations = pm.Normal("observations", mu=mean, sd=std, observed=observed_data)

    # MCMCを使用して後方分布からサンプリング
    trace = pm.sample(500)

# 結果の要約
print(pm.summary(trace))
