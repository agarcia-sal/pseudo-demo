def sum_to_n(integer_n: int) -> int:
    total_sum: int = 0
    current_number: int = 0

    while current_number <= integer_n:
        total_sum += current_number
        current_number += 1

    return total_sum