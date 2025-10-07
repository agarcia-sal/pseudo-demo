from typing import List


def count_up_to(q: int) -> List[int]:
    result_list: List[int] = []
    current_number: int = 2
    while current_number < q:
        flag_prime: bool = True
        divisor: int = 2
        while divisor < current_number and flag_prime:
            if current_number % divisor == 0:
                flag_prime = False
                break
            divisor += 1
        if flag_prime:
            result_list.append(current_number)
        current_number += 1
    return result_list