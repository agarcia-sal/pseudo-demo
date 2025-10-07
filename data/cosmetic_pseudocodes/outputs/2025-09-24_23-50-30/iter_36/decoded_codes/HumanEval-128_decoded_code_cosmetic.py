from typing import Iterable, Optional

def prod_sign(collection_of_numbers: Iterable[int]) -> Optional[int]:
    def compute_sign(items: Iterable[int]) -> Optional[int]:
        items_list = list(items)
        if not items_list:
            return None
        if 0 in items_list:
            return 0

        def count_negatives(seq: Iterable[int], accumulator: int) -> int:
            seq_list = list(seq)
            if not seq_list:
                return accumulator
            return count_negatives(seq_list[1:], accumulator + (1 if seq_list[0] < 0 else 0))

        negatives_count = count_negatives(items_list, 0)
        return 1 if negatives_count % 2 == 0 else -1

    def total_absolute(items: Iterable[int], index: int, acc: int) -> int:
        items_list = list(items)
        if index == len(items_list):
            return acc
        return total_absolute(items_list, index + 1, acc + abs(items_list[index]))

    sign_value = compute_sign(collection_of_numbers)
    if sign_value is None:
        return None
    magnitude_sum = total_absolute(collection_of_numbers, 0, 0)
    return sign_value * magnitude_sum