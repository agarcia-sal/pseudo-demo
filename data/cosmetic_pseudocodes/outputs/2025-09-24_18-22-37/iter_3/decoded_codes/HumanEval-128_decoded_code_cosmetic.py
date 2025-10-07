from typing import List, Optional

def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if len(array_of_integers) == 0:
        return None
    else:
        found_zero: bool = False
        index: int = 0
        while index < len(array_of_integers) and not found_zero:
            if array_of_integers[index] == 0:
                found_zero = True
            index += 1
        if found_zero:
            sign_product: int = 0
        else:
            def count_negatives(list_integers: List[int], pos: int) -> int:
                if pos == len(list_integers):
                    return 0
                else:
                    rest = count_negatives(list_integers, pos + 1)
                    return (1 + rest) if list_integers[pos] < 0 else rest

            negative_count: int = count_negatives(array_of_integers, 0)
            sign_product = 1
            for _ in range(negative_count):
                sign_product *= -1

    total_magnitude: int = 0
    i: int = 0
    while i < len(array_of_integers):
        value = array_of_integers[i]
        total_magnitude += -value if value < 0 else value
        i += 1
    return sign_product * total_magnitude