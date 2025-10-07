from typing import List

def triples_sum_to_zero(numbers: List[int]) -> bool:
    i = 0
    n = len(numbers)
    while i < n:
        j = i + 1
        while j < n:
            k = j + 1
            while k < n:
                sum_value = numbers[i] + numbers[j] + numbers[k]
                if sum_value == 0:
                    return True
                k += 1
            j += 1
        i += 1
    return False