from typing import List, Tuple


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        def multiply_list_first(list_𝛂: List[int], multiplier_ζ: int) -> List[int]:
            if list_𝛂:
                head_π, tail_λ = list_𝛂[0], list_𝛂[1:]
                return [head_π * multiplier_ζ] + tail_λ
            else:
                return []

        def sum_recursive(ξ: List[int]) -> int:
            if not ξ:
                return 0
            hd_σ, tl_τ = ξ[0], ξ[1:]
            return hd_σ + sum_recursive(tl_τ)

        def abs_and_sign(n_ί: int, acc_ω: int) -> Tuple[int, int]:
            if n_ί < 0:
                return (-n_ί, acc_ω * -1)
            else:
                return (n_ί, acc_ω)

        val_ξ, multiplier_μ = abs_and_sign(integer_value, 1)
        str_digits_ϕ = str(val_ξ)

        def str_to_int_list(str_ρ: str, acc_𝜈: List[int]) -> List[int]:
            if str_ρ == "":
                acc_𝜈.reverse()
                return acc_𝜈
            head_chr = str_ρ[0]
            tail_str = str_ρ[1:]
            digit_int = ord(head_chr) - ord('0')
            return str_to_int_list(tail_str, [digit_int] + acc_𝜈)

        digits_list_θ = str_to_int_list(str_digits_ϕ, [])
        adjusted_digits_υ = multiply_list_first(digits_list_θ, multiplier_μ)
        return sum_recursive(adjusted_digits_υ)

    def filter_gt_zero(lst_κ: List[int]) -> List[int]:
        if not lst_κ:
            return []
        hd_β, tl_γ = lst_κ[0], lst_κ[1:]
        filtered_tail = filter_gt_zero(tl_γ)
        if hd_β > 0:
            return [hd_β] + filtered_tail
        else:
            return filtered_tail

    def map_digits_sum(lst_δ: List[int], acc_ν: List[int]) -> List[int]:
        if not lst_δ:
            acc_ν.reverse()
            return acc_ν
        hd_ψ, tl_ω = lst_δ[0], lst_δ[1:]
        return map_digits_sum(tl_ω, [digits_sum(hd_ψ)] + acc_ν)

    digit_sums_list = map_digits_sum(array_of_integers, [])
    filtered_nonzero = filter_gt_zero(digit_sums_list)

    def length_counter(lst_λ: List[int], cnt_μ: int) -> int:
        if not lst_λ:
            return cnt_μ
        _, tail_ν = lst_λ[0], lst_λ[1:]
        return length_counter(tail_ν, cnt_μ + 1)

    return length_counter(filtered_nonzero, 0)