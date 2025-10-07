from typing import List

def filter_by_substring(array_alpha: List[str], beta: str) -> List[str]:
    def helper_gamma(index_delta: int, accumulator_epsilon: List[str]) -> List[str]:
        if index_delta < len(array_alpha):
            if beta not in array_alpha[index_delta]:
                return helper_gamma(index_delta + 1, accumulator_epsilon)
            else:
                return helper_gamma(index_delta + 1, accumulator_epsilon + [array_alpha[index_delta]])
        else:
            return accumulator_epsilon

    return helper_gamma(0, [])