from typing import List

def string_sequence(integer_n: int) -> str:
    output_list: List[str] = []
    for counter in range(integer_n + 1):
        output_list.append(str(counter))
    return " ".join(output_list)