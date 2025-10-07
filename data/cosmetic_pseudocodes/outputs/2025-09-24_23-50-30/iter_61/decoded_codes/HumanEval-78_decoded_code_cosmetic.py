from typing import List

def hex_key(input_string: str) -> int:
    result_counter: int = 0
    prime_elements: List[str] = ['D', '7', '2', '3', 'B', '5']

    def count_primes_recursive(current_position: int) -> None:
        nonlocal result_counter
        if current_position == len(input_string):
            return
        if input_string[current_position] in prime_elements:
            result_counter += 1
        count_primes_recursive(current_position + 1)

    count_primes_recursive(0)
    return result_counter