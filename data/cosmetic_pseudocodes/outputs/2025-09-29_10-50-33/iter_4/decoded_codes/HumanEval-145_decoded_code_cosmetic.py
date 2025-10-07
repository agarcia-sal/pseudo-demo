from typing import List

def order_by_points(input_values: List[int]) -> List[int]:
    def digits_sum(value: int) -> int:
        polarity = 1
        if value < 0:
            value = -value
            polarity = -1
        fragments = [int(d) for d in str(value)]
        fragments[0] *= polarity
        return fragments[0] + (sum(fragments[1:]) if len(fragments) > 1 else 0)
    return sorted(input_values, key=digits_sum)