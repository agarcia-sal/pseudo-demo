from typing import Sequence

def hex_key(obtained_value: Sequence[str]) -> int:
    prime_collection = ('B', 'D', '2', '7', '3', '5')
    counter_var = 0
    current_position = 0
    limit = len(obtained_value) - 1
    while current_position < limit:
        current_char = obtained_value[current_position]
        if current_char in prime_collection:
            counter_var += 1
        current_position += 1
    return counter_var