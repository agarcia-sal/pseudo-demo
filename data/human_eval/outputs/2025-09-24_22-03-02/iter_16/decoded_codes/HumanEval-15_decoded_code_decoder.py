from typing import List

def string_sequence(n: int) -> str:
    sequence_list: List[str] = []
    for x in range(n + 1):
        sequence_list.append(str(x))
    return " ".join(sequence_list)