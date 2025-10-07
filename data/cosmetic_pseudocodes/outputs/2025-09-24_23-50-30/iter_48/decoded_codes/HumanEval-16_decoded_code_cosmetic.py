from typing import List

def count_distinct_characters(captured_input: str) -> int:
    auxiliary_list: List[str] = []
    index_counter: int = 1
    while not (index_counter > len(captured_input)):
        auxiliary_list.append(captured_input[index_counter - 1].lower())
        index_counter += 1
    unique_chars = set()
    for element in auxiliary_list:
        unique_chars.add(element)
    return len(unique_chars)