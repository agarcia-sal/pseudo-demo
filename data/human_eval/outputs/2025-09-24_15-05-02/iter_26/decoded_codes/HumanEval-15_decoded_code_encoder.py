from typing import List

def string_sequence(n: int) -> str:
    return ' '.join(str(number) for number in range(n + 1))