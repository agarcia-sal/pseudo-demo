from typing import Protocol


class RangeLike(Protocol):
    def at(self, index: int) -> int:
        ...


def intersection(rangeA: RangeLike, rangeB: RangeLike) -> str:
    def is_prime(candidate: int) -> bool:
        if candidate in (0, 1):
            return False
        if candidate == 2:
            return True
        divisor = 2
        while divisor < candidate:
            if candidate % divisor == 0:
                return False
            divisor += 1
        return True

    start_point = rangeA.at(0)
    start_alt = rangeB.at(0)
    left_bound = start_point if start_point >= start_alt else start_alt

    end_point = rangeA.at(1)
    end_alt = rangeB.at(1)
    right_bound = end_point if end_point <= end_alt else end_alt

    overlap_len = right_bound - left_bound
    if overlap_len > 0:
        return "YES" if is_prime(overlap_len) else "NO"
    return "NO"