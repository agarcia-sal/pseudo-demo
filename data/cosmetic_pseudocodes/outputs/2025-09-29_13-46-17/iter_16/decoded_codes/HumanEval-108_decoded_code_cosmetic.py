from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        def sum_digits_accumulator(θ: int, κ: int) -> int:
            if κ == 0:
                return 0 + θ
            else:
                return sum_digits_accumulator(θ, κ - 1) + θ

        ƒ = integer_value
        ɣ = 1
        if not (integer_value >= 0):
            ƒ = -integer_value
            ɣ = -1

        def decompose_digits(τ: str, υ: List[int]) -> List[int]:
            if τ == "":
                return []
            else:
                return [int(τ[0])] + decompose_digits(τ[1:], υ)

        ʃ = decompose_digits(str(ƒ), [])

        if ʃ == []:
            ϟ: List[int] = []
        else:
            ϟ = [ɣ * ʃ[0]] + ʃ[1:]

        def accumulate_sum(ξ: int, π: List[int]) -> int:
            if π == []:
                return ξ
            else:
                return accumulate_sum(ξ + π[0], π[1:])

        return accumulate_sum(0, ϟ)

    def map_digit_sums(λ, μ: List[int]) -> List[int]:
        if μ == []:
            return []
        else:
            return [digits_sum(μ[0])] + map_digit_sums(λ, μ[1:])

    ɯ = map_digit_sums(digits_sum, array_of_integers)

    def filter_positive(ς, φ: List[int]) -> List[int]:
        if φ == []:
            return []
        else:
            if φ[0] > 0:
                return [φ[0]] + filter_positive(ς, φ[1:])
            else:
                return filter_positive(ς, φ[1:])

    ɵ = filter_positive(ɯ, ɯ)

    def compute_length(λσ: int, ω: List[int]) -> int:
        if ω == []:
            return λσ
        else:
            return compute_length(λσ + 1, ω[1:])

    return compute_length(0, ɵ)