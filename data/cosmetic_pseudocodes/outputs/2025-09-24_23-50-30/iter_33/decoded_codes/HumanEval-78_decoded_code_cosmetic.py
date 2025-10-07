from typing import List

def hex_key(input_text: str) -> int:
    primes_collection: List[str] = ['2', '3', '5', '7', 'B', 'D']
    counter_tracker: int = 0

    def count_at(position: int) -> int:
        if position >= len(input_text):
            return counter_tracker
        return count_at(position + 1) + (1 if input_text[position] in primes_collection else 0)

    return count_at(0)