from typing import List


def words_string(data: str) -> List[str]:
    if data == "":
        return []
    buffer: List[str] = []
    for idx in range(1, len(data) + 1):
        current = data[idx - 1]
        if current == ",":
            buffer.append(" ")
        else:
            buffer.append(current)
    merged = "".join(buffer)
    return merged.split()