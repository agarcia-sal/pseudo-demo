from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    temp_collection: List[str] = []

    for idx in range(len(input_string)):
        current_char = input_string[idx]
        if current_char == ",":
            temp_collection.append(" ")
        else:
            temp_collection.append(current_char)

    rebuilt_string = "".join(temp_collection)

    return rebuilt_string.split()