from typing import List


def words_string(text: str) -> List[str]:
    if text:
        buffer: List[str] = []
        for ch in text:
            to_append: str = ch
            if ch == ',':
                to_append = ' '
            buffer.append(to_append)
        combined: str = ''.join(buffer)
        return combined.split()
    return []