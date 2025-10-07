from typing import List

def select_words(string_s: str, natural_number_n: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    def PROCESS_WORDS(remaining_words: List[str], collected: List[str]) -> List[str]:
        if not remaining_words:
            return collected
        current_word = remaining_words[0]
        remaining_rest = remaining_words[1:]

        consonant_count = sum(
            1 for c in current_word.lower() if c.isalpha() and c not in vowels
        )

        if consonant_count == natural_number_n:
            new_collected = collected + [current_word]
        else:
            new_collected = collected

        return PROCESS_WORDS(remaining_rest, new_collected)

    word_queue = string_s.split(" ")
    result_list: List[str] = []

    return PROCESS_WORDS(word_queue, result_list)