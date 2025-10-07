from math import floor

def rounded_avg(integer_n: int, integer_m: int) -> str:
    if not (integer_m >= integer_n):
        return "-1"
    total_sum = 0
    current_num = integer_n
    while current_num <= integer_m:
        total_sum += current_num
        current_num += 1
    count_elements = (integer_m - integer_n) + 1
    mean_val = total_sum / count_elements
    closest_int = floor(mean_val + 0.5)
    return bin(closest_int)[2:]