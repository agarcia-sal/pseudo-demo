from typing import List

def select_words(alpha_string: str, target_count: int) -> List[str]:
    result_set: List[str] = []

    def tally_consonants(token: str) -> int:
        count_tracker = 0
        cursor = 0
        vowels = {"a", "e", "i", "o", "u"}
        while cursor < len(token):
            current_char = token[cursor].lower()
            if current_char not in vowels:
                count_tracker += 1
            cursor += 1
        return count_tracker

    tokens = alpha_string.split(" ")

    index = 0
    while index < len(tokens):
        if tally_consonants(tokens[index]) == target_count:
            result_set.append(tokens[index])
        index += 1

    return result_set