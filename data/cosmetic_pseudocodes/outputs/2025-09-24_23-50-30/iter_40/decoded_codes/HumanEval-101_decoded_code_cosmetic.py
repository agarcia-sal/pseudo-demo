from typing import List


def words_string(param: str) -> List[str]:
    if param == "":
        return []

    buffer: List[str] = []
    for idx in range(len(param)):
        if param[idx] == ",":
            buffer.append(" ")
        else:
            buffer.append(param[idx])

    combined = "".join(buffer)

    output: List[str] = []
    temp_word = ""
    for ch in combined:
        if ch not in {" ", "\t", "\n"}:
            temp_word += ch
        elif temp_word:
            output.append(temp_word)
            temp_word = ""
    if temp_word:
        output.append(temp_word)

    return output