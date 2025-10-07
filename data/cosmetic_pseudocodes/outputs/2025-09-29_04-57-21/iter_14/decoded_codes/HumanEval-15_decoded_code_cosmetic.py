from typing import List

def string_sequence(integer_n: int) -> str:
    counter: int = 0
    parts: List[str] = []
    while counter <= integer_n:
        parts.append(str(counter))
        counter += 1
    result: str = " ".join(parts)
    return result