from typing import List

def string_sequence(integer_n: int) -> str:
    auxiliary_list: List[str] = []
    for iterator in range(integer_n + 1):
        auxiliary_list.append(str(iterator))
    return ' '.join(auxiliary_list)