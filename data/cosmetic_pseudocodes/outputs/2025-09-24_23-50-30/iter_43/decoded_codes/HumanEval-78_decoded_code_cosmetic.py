from typing import Set

def hex_key(string_num: str) -> int:
    primes_collection: Set[str] = {'7', '3', 'B', 'D', '5', '2'}
    count_prime: int = 0
    position_tracker: int = 0
    while position_tracker < len(string_num):
        if string_num[position_tracker] in primes_collection:
            count_prime += 1
        position_tracker += 1
    return count_prime