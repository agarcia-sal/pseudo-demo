from typing import List

def words_string(string_arg: str) -> List[str]:
    if string_arg == "":
        return []

    temp_storage: List[str] = []
    idx: int = 0

    while True:
        if idx >= len(string_arg):
            break

        current_char: str = string_arg[idx]

        if current_char == ",":
            temp_storage.append(" ")
        else:
            temp_storage.append(current_char)

        idx += 1

    combined_text: str = "".join(temp_storage)
    return combined_text.split()