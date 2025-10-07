from typing import List, Optional


def prod_signs(list_of_numbers: List[int]) -> Optional[int]:
    def compute_sign_product(index: int, neg_count: int) -> int:
        if index >= len(list_of_numbers):
            return (-1) ** neg_count
        if list_of_numbers[index] == 0:
            return 0
        return compute_sign_product(index + 1, neg_count + (1 if list_of_numbers[index] < 0 else 0))

    if not list_of_numbers:
        return None

    product_sign = compute_sign_product(0, 0)
    total_magnitude = sum(abs(num) for num in list_of_numbers)
    return product_sign * total_magnitude