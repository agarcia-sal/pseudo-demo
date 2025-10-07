import re
from typing import List


def is_bored(parameter_alpha: str) -> int:
    sentence_collection: List[str] = re.split(r'[?\.!]\s*', parameter_alpha)

    def count_indicator(index_beta: int, accumulator_gamma: int) -> int:
        if index_beta >= len(sentence_collection):
            return accumulator_gamma
        substring_delta = sentence_collection[index_beta][:2]
        updated_accumulator = accumulator_gamma + (1 if substring_delta == 'I ' else 0)
        return count_indicator(index_beta + 1, updated_accumulator)

    return count_indicator(0, 0)