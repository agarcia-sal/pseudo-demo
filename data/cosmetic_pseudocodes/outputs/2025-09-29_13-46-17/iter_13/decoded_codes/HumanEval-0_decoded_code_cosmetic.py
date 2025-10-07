from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    def recursive_outer_loop(λμψ: int, αξ: float) -> bool:
        if λμψ >= len(list_of_numbers):
            return False
        return recursive_inner_loop(λμψ, 0, αξ)

    def recursive_inner_loop(λμψ: int, θζ: int, αξ: float) -> bool:
        if θζ >= len(list_of_numbers):
            return recursive_outer_loop(λμψ + 1, αξ)
        if λμψ != θζ:
            ωρ = list_of_numbers[λμψ]
            βη = list_of_numbers[θζ]
            κσ = ωρ - βη if ωρ >= βη else βη - ωρ
            if κσ < threshold_value:
                return True
        return recursive_inner_loop(λμψ, θζ + 1, αξ)

    return recursive_outer_loop(0, threshold_value)