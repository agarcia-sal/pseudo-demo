from typing import List


def select_words(string_s: str, natural_number_n: int) -> List[str]:
    def consonant_count(chars: str, position: int, count: int) -> int:
        if position >= len(chars):
            return count
        current_char = chars[position].lower()
        updated_count = count + (1 if current_char not in {"a", "e", "i", "o", "u"} else 0)
        return consonant_count(chars, position + 1, updated_count)

    def process_words(words_list: List[str], idx: int, collected: List[str]) -> List[str]:
        if idx >= len(words_list):
            return collected
        candidate = words_list[idx]
        if consonant_count(candidate, 0, 0) == natural_number_n:
            return process_words(words_list, idx + 1, collected + [candidate])
        return process_words(words_list, idx + 1, collected)

    return process_words(string_s.split(" "), 0, [])