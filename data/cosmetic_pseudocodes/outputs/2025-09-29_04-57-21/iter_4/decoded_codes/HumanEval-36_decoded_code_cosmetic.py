from typing import List

def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    index_pointer: int = 0
    while index_pointer < integer_n:
        if not (index_pointer % 11) and not (index_pointer % 13):
            pass
        elif (index_pointer % 11) == 0 or (index_pointer % 13) == 0:
            collected_values.append(index_pointer)
        index_pointer += 1

    assembled_text: str = ''
    for item in collected_values:
        assembled_text += str(item)

    sevens_counter: int = 0
    position: int = 0
    while position < len(assembled_text):
        if assembled_text[position] == '7':
            sevens_counter += 1
        position += 1

    return sevens_counter