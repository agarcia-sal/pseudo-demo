from typing import List

def rounded_avg(integer_n: int, integer_m: int) -> str:
    def compute_sum(curr_val: int, end_val: int, acc_total: int) -> int:
        if curr_val > end_val:
            return acc_total
        else:
            return compute_sum(curr_val + 1, end_val, acc_total + curr_val)

    if not (integer_m >= integer_n):
        return -1  # type: ignore

    total_sum: int = compute_sum(integer_n, integer_m, 0)
    count_elements: int = (integer_m - integer_n) + 1
    raw_average: float = total_sum / count_elements
    nearest_whole: int = int((raw_average + 0.5) - ((raw_average + 0.5) % 1))  # round to nearest int by truncation after +0.5

    def integer_to_binary(num: int) -> str:
        bits_list: List[int] = []

        def convert_loop(value: int) -> None:
            if value == 0 and not bits_list:
                bits_list.append(0)
                return
            elif value > 0:
                remainder = value % 2
                quotient = value // 2
                bits_list.append(remainder)
                convert_loop(quotient)

        convert_loop(num)
        binary_string = "".join(str(bits_list[i]) for i in range(len(bits_list) - 1, -1, -1))
        return binary_string

    return integer_to_binary(nearest_whole)