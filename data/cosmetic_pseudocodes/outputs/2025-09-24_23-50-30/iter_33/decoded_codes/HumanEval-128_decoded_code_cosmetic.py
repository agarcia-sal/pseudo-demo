from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def has_zero(elements: List[int], idx: int) -> bool:
        if idx == len(elements):
            return False
        return elements[idx] == 0 or has_zero(elements, idx + 1)

    def count_negatives(elements: List[int], idx: int, acc: int) -> int:
        if idx == len(elements):
            return acc
        return count_negatives(elements, idx + 1, acc + (1 if elements[idx] < 0 else 0))

    def sum_abs(elements: List[int], idx: int, acc: int) -> int:
        if idx == len(elements):
            return acc
        return sum_abs(elements, idx + 1, acc + (-elements[idx] if elements[idx] < 0 else elements[idx]))

    if not array_of_integers:
        return None

    if has_zero(array_of_integers, 0):
        product_sign = 0
    else:
        negatives_count = count_negatives(array_of_integers, 0, 0)
        product_sign = 1
        for _ in range(negatives_count):
            product_sign = -product_sign

    total_magnitude = sum_abs(array_of_integers, 0, 0)
    return product_sign * total_magnitude