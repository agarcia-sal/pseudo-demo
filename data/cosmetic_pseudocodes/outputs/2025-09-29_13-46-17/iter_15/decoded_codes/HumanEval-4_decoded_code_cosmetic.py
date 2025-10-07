from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    def recur_accum(idx_λ: int, acc_ϕ: float) -> float:
        if idx_λ >= len(list_of_numbers):
            return acc_ϕ
        current_ω = list_of_numbers[idx_λ]
        return recur_accum(idx_λ + 1, acc_ϕ + current_ω)

    def recur_abs_sum(idx_Ψ: int, acc_π: float, mean_θ: float) -> float:
        if idx_Ψ >= len(list_of_numbers):
            return acc_π
        element_𝛿 = list_of_numbers[idx_Ψ]
        raw_diff_ζ = element_𝛿 - mean_θ
        abs_diff_η = -raw_diff_ζ if raw_diff_ζ < 0 else raw_diff_ζ
        return recur_abs_sum(idx_Ψ + 1, acc_π + abs_diff_η, mean_θ)

    n_ℵ = len(list_of_numbers)
    if n_ℵ == 0:
        return 0.0

    sum_total_β = recur_accum(0, 0.0)
    mean_μ = sum_total_β / n_ℵ
    absolute_total_γ = recur_abs_sum(0, 0.0, mean_μ)
    mad_val_Ω = absolute_total_γ / n_ℵ

    return mad_val_Ω