from typing import Union


def rounded_avg(xy: int, zw: int) -> Union[str, int]:
    def compute_sum(a: int, b: int, acc: int) -> int:
        if a > b:
            return acc
        return compute_sum(a + 1, b, acc + a)

    if zw < xy:
        return -1

    total_sum: int = compute_sum(xy, zw, 0)
    count: int = (zw - xy) + 1
    mean_val: float = total_sum / count
    # Round to nearest integer with half up, handling negatives correctly
    nearest_int: int = int((mean_val + 0.5) // 1) - (1 if mean_val < 0 else 0)
    bin_str: str = format(nearest_int, 'b')
    return bin_str