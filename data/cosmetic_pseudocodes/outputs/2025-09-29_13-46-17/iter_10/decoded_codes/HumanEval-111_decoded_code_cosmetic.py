from typing import List, Dict


def histogram(test_string: str) -> Dict[str, int]:
    def count_occurrences(words: List[str]) -> int:
        if not words:
            return 0
        first = words[0]
        rest = words[1:]
        return 1 + count_occurrences(rest) if first in rest else 1

    words: List[str] = test_string.split(' ')
    freq_map: Dict[str, int] = {}
    length: int = len(words)

    max_count: int = 0
    index: int = 0

    while index < length:
        word = words[index]
        if word and count_occurrences([w for w in words if w == word]) > max_count:
            max_count = count_occurrences([w for w in words if w == word])
        index += 1

    if max_count > 0:
        index = 0
        while index < length:
            word = words[index]
            if count_occurrences([w for w in words if w == word]) == max_count:
                freq_map[word] = max_count
            index += 1

    return freq_map