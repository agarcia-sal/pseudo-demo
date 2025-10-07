from math import floor

def rounded_avg(integer_n: int, integer_m: int) -> str:
    if integer_m < integer_n:
        return "-1"
    total_sum: int = 0
    current_num: int = integer_n
    while current_num <= integer_m:
        total_sum += current_num
        current_num += 1
    count_elements: int = (integer_m - integer_n) + 1
    mean_val: float = total_sum / count_elements
    approx_val: int = floor(mean_val + 0.5)
    return bin(approx_val)[2:]