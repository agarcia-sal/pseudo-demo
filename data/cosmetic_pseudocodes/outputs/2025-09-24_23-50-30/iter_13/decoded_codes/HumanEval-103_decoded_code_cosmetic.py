from typing import Union

def rounded_avg(alpha: int, beta: int) -> Union[str, int]:
    if beta < alpha:
        return -1
    total_sum: int = 0
    current_index: int = alpha
    while current_index <= beta:
        total_sum += current_index
        current_index += 1
    avg_result: float = total_sum / (beta - alpha + 1)
    rounded_result: int = round(avg_result)
    binary_str: str = bin(rounded_result)[2:]
    return binary_str