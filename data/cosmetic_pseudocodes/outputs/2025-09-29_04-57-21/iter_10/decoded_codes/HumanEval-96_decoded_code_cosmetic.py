from typing import List

def count_up_to(n: int) -> List[int]:
    prime_numbers: List[int] = []
    current_value: int = 2
    while current_value < n:
        flag_prime: bool = True
        divisor_candidate: int = 2
        while divisor_candidate < current_value:
            if current_value % divisor_candidate == 0:
                flag_prime = False
                break
            divisor_candidate += 1
        if flag_prime:
            prime_numbers.append(current_value)
        current_value += 1
    return prime_numbers