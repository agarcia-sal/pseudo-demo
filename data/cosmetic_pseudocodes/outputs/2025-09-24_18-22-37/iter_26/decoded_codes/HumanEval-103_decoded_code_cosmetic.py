from typing import Union


def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    if beta >= alpha:
        total_sum: int = 0
        current_num: int = alpha
        while current_num <= beta:
            temp_sum: int = total_sum
            total_sum = temp_sum + current_num
            current_num += 1
        range_length: int = beta - alpha + 1
        avg: float = total_sum / range_length
        nearest_int: int = round(avg)
        binary_str: str = bin(nearest_int)[2:] if nearest_int >= 0 else '-' + bin(-nearest_int)[2:]
        return binary_str
    else:
        return -1