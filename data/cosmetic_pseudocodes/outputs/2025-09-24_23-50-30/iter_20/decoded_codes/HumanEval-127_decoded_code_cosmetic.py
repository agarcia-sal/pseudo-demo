from typing import List, Union


def intersection(paramA: List[int], paramB: List[int]) -> Union[str, str]:
    def is_prime(value: int) -> bool:
        if value < 2:
            return False
        if value == 2:
            return True
        for k in range(2, value):
            if value % k == 0:
                return False
        return True

    start_point: int = paramA[0]
    alt_start: int = paramB[0]
    left_limit: int = start_point if start_point >= alt_start else alt_start

    end_point: int = paramA[1]
    alt_end: int = paramB[1]
    right_limit: int = end_point if end_point <= alt_end else alt_end

    length_of_overlap: int = right_limit - left_limit
    if length_of_overlap > 0 and is_prime(length_of_overlap):
        return "YES"
    else:
        return "NO"