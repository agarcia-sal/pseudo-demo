from typing import List


def select_words(text_input: str, count_target: int) -> List[str]:
    accumulator: List[str] = []

    def count_consonants(token: str, position: int, tally: int) -> int:
        if position >= len(token):
            return tally
        # Check if current character is a consonant (not a vowel)
        if token[position].lower() not in {"a", "e", "i", "o", "u"}:
            return count_consonants(token, position + 1, tally + 1)
        return count_consonants(token, position + 1, tally)

    def process_tokens(tokens: List[str], index: int) -> None:
        if index >= len(tokens):
            return
        current_token = tokens[index]
        consonant_total = count_consonants(current_token, 0, 0)
        if consonant_total == count_target:
            accumulator.append(current_token)
        process_tokens(tokens, index + 1)

    word_list = text_input.split(" ")
    process_tokens(word_list, 0)

    return accumulator