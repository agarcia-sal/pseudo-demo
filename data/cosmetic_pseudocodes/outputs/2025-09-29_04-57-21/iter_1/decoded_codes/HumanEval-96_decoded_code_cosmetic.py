from typing import List


def count_up_to(n: int) -> List[int]:
    prime_numbers: List[int] = []
    for current_num in range(2, n):
        prime_flag = True
        for divisor in range(2, current_num):
            if current_num % divisor == 0:
                prime_flag = False
                break
        if prime_flag:
            prime_numbers.append(current_num)
    return prime_numbers