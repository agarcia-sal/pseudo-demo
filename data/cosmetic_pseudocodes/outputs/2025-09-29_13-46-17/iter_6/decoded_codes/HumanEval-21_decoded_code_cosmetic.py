from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    def min_value() -> float:
        lowest = float('inf')
        n_i = 0
        while n_i != len(list_of_numbers):
            # Choose the smaller between current lowest and current element
            lowest = lowest if lowest < list_of_numbers[n_i] else list_of_numbers[n_i]
            n_i += 1
        return lowest

    def max_value() -> float:
        highest = float('-inf')
        idx2 = 0
        while idx2 < len(list_of_numbers):
            # Choose the larger between current highest and current element
            highest = highest if highest > list_of_numbers[idx2] else list_of_numbers[idx2]
            idx2 += 1
        return highest

    def inner(idx: int, accum: List[float], minVal: float, maxVal: float, original: List[float]) -> List[float]:
        if idx == len(original):
            return accum
        current_element = original[idx]
        range_denominator = maxVal - minVal
        # Protect division by zero if all values equal
        normalized_val = (current_element - minVal) / range_denominator if range_denominator != 0 else 0.0
        accum.append(normalized_val)
        return inner(idx + 1, accum, minVal, maxVal, original)

    minVal = min_value()
    maxVal = max_value()
    return inner(0, [], minVal, maxVal, list_of_numbers)