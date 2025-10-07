from typing import List

def words_string(input_string: str) -> List[str]:
    if len(input_string) == 0:
        return []

    temp_container: List[str] = []

    i: int = 0
    while i < len(input_string):
        current_char = input_string[i]
        if current_char == ',':
            temp_container.append(' ')
        else:
            temp_container.append(current_char)
        i += 1

    merged_text = "".join(temp_container)
    return merged_text.split(' ')