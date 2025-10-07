from typing import List

def string_sequence(integer_n: int) -> str:
    result: List[str] = [str(counter) for counter in range(integer_n + 1)]
    output: str = " ".join(result)
    return output