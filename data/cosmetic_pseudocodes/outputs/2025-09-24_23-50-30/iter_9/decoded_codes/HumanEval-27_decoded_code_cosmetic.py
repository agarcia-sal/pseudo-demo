from typing import List

def flip_case(alternate_input: str) -> str:
    result_collection: List[str] = []
    for index in range(len(alternate_input)):
        current_char = alternate_input[index]
        if current_char == current_char.lower():
            result_collection.append(current_char.upper())
        else:
            result_collection.append(current_char.lower())
    return ''.join(result_collection)