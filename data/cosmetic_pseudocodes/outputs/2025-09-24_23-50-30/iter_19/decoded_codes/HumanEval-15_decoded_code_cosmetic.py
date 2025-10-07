from typing import List

def string_sequence(integer_n: int) -> str:
    output_list: List[str] = [str(counter) for counter in range(integer_n + 1)]
    result: str = " ".join(output_list)
    return result