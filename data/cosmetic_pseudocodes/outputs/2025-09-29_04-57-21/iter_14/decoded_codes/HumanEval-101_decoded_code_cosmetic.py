from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string != "":
        temp_storage: List[str] = []
        idx: int = 0

        while idx < len(input_string):
            current_char: str = input_string[idx]

            if current_char != ",":
                temp_storage.append(current_char)
            else:
                temp_storage.append(" ")

            idx += 1

        combined: str = ""
        count: int = 0

        while count < len(temp_storage):
            combined += temp_storage[count]
            count += 1

        return combined.split()

    return []