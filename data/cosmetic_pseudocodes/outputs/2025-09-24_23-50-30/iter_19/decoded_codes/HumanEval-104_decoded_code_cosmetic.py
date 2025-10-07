from typing import List

def unique_digits(values: List[int]) -> List[int]:
    results: List[int] = []
    idx: int = 0
    while idx < len(values):
        number = values[idx]
        digits_set = set(str(number))
        isAllOdd = True
        for digit_char in digits_set:
            if (int(digit_char) % 2) == 0:
                isAllOdd = False
                break
        if isAllOdd:
            results.append(number)
        idx += 1
    return sorted(results)