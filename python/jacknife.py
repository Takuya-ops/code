import numpy as np

# データセット
data = np.array([4, 7, 2, 6, 3])

# ジャックナイフ推定
n = len(data)
jackknife_estimates = np.array([np.mean(np.delete(data, i)) for i in range(n)])

# ジャックナイフ推定値の平均と標準誤差
mean_estimate = np.mean(jackknife_estimates)
std_error = np.sqrt((n - 1) * np.mean((jackknife_estimates - mean_estimate) ** 2))

print(f"ジャックナイフ推定値の平均: {mean_estimate}")
print(f"ジャックナイフ推定の標準誤差: {std_error}")
