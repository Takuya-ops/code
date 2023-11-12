def calculate_phi_coefficient(table):
    # 分割表から値を取得
    a, b = table[0]
    c, d = table[1]

    # ファイ係数の計算
    numerator = a * d - b * c
    denominator = ((a + b) * (a + c) * (b + d) * (c + d)) ** 0.5
    phi = numerator / denominator
    return phi


# 2x2分割表の例
contingency_table = [
    [10, 5],  # 例えば、病気ありの人の変異あり、変異なしの人数
    [20, 40],
]  # 病気なしの人の変異あり、変異なしの人数

# ファイ係数の計算
phi_coefficient = calculate_phi_coefficient(contingency_table)
print("ファイ係数:", phi_coefficient)


# 既存モジュールを使用する場合
import scipy.stats as stats

# 2x2の分割表
contingency_table = [[10, 5], [20, 40]]  # 例：病気ありの人の変異あり、変異なしの人数  # 病気なしの人の変異あり、変異なしの人数

# ファイ係数の計算
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
total_sum = sum([sum(row) for row in contingency_table])  # 全要素の合計
phi_coefficient = (chi2 / total_sum) ** 0.5

print("ファイ係数:", phi_coefficient)
