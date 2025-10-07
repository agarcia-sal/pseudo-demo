from typing import Tuple


def hex_key(input_string: str) -> int:
    prime_characters: Tuple[str, ...] = ('D', '7', '3', '5', 'B', '2')
    count_prime_occurrences: int = 0
    pos_counter: int = 0
    length: int = len(input_string)

    while pos_counter < length:
        current_char: str = input_string[pos_counter]
        is_in_primes: bool = False
        for prime_index in range(len(prime_characters)):
            if current_char == prime_characters[prime_index]:
                is_in_primes = True
                break
        if is_in_primes:
            count_prime_occurrences += 1
        pos_counter += 1

    return count_prime_occurrences