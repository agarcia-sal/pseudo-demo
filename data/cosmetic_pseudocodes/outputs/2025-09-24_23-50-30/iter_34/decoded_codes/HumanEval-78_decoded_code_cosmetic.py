from typing import Dict

def hex_key(hashcode: str) -> int:
    prime_set: Dict[str, bool] = {'2': True, '3': True, '5': True, '7': True, 'B': True, 'D': True}
    count_accumulator: int = 0
    position: int = 0
    while position < len(hashcode):
        if hashcode[position] in prime_set:
            count_accumulator += 1
        position += 1
    return count_accumulator