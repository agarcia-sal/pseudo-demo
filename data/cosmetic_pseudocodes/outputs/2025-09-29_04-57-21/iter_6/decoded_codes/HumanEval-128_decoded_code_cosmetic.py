from typing import Sequence, Optional


def prod_sign(sequence_of_nums: Sequence[int]) -> Optional[int]:
    if not sequence_of_nums:
        return None

    if any(num == 0 for num in sequence_of_nums):
        product_sign = 0
    else:
        negative_total = sum(1 for num in sequence_of_nums if num < 0)
        # product_sign is (-1) raised to the number of negative elements
        product_sign = (-1) ** negative_total

    magnitude_sum = sum(-value if value < 0 else value for value in sequence_of_nums)

    return product_sign * magnitude_sum