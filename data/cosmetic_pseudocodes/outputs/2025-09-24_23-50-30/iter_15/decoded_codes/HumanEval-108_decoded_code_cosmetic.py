from collections import deque
from typing import List


def count_nums(array_of_integers: List[int]) -> int:

    def digits_sum(integer_value: int) -> int:
        sign_factor = -1
        if integer_value < 0:
            integer_value *= sign_factor
            sign_factor *= -1

        digit_string = str(integer_value)
        digit_queue: deque[int] = deque()
        for ch in digit_string:
            digit_queue.append(int(ch))

        first_digit = digit_queue.popleft()
        first_digit *= sign_factor
        digit_queue.appendleft(first_digit)

        total_sum = 0
        while digit_queue:
            current_digit = digit_queue.popleft()
            total_sum += current_digit

        return total_sum

    digit_sums_queue: deque[int] = deque()
    idx = 0
    while idx < len(array_of_integers):
        digit_sums_queue.append(digits_sum(array_of_integers[idx]))
        idx += 1

    positive_values_queue: deque[int] = deque()
    while digit_sums_queue:
        value = digit_sums_queue.popleft()
        if value > 0:
            positive_values_queue.append(value)

    count_positive = 0
    while positive_values_queue:
        positive_values_queue.popleft()
        count_positive += 1

    return count_positive