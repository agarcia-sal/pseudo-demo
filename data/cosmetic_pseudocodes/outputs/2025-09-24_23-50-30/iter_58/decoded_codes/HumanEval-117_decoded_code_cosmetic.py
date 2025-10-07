from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def count_consonants(str_x: str) -> int:
        count_y = 0
        for ch in str_x:
            if ch.lower() not in {"a", "e", "i", "o", "u"}:
                count_y += 1
        return count_y

    list_z: List[str] = [
        element_w for element_w in string_s.split(" ") if count_consonants(element_w) == natural_number_n
    ]
    return list_z