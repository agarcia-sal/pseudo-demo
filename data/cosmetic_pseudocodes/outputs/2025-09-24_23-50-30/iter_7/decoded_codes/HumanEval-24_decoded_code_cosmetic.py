from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    list_m = list(range(1, integer_n))

    def search_divisor(index_k: int) -> Optional[int]:
        if index_k < 0:
            return None
        if integer_n % list_m[index_k] == 0:
            return list_m[index_k]
        return search_divisor(index_k - 1)

    return search_divisor(len(list_m) - 1)