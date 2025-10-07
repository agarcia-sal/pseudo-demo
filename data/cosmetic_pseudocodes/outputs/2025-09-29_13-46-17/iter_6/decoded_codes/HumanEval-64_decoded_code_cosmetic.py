from typing import Dict

def vowels_count(string_input: str) -> int:
    variAble_map_1: Dict[str, int] = {
        "a": 1, "e": 1, "i": 1, "o": 1, "u": 1,
        "A": 1, "E": 1, "I": 1, "O": 1, "U": 1
    }

    def innerSum(idx_accumulator: int, acc_sum: int) -> int:
        if idx_accumulator < 0:
            return acc_sum
        currentChar = string_input[idx_accumulator]
        charExistence = 0 + (currentChar in variAble_map_1)
        return innerSum(idx_accumulator - 1, acc_sum + charExistence)

    if not string_input:
        return 0
    lastChar = string_input[-1]
    baseSum = innerSum(len(string_input) - 1, 0)
    additional = int(lastChar == "y" or lastChar == "Y")
    return baseSum + additional