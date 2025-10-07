from typing import List


def anti_shuffle(input_string: str) -> str:
    tokens: List[str] = input_string.split(' ')
    processed_words: List[str] = []

    def process_word(index: int) -> None:
        if index >= len(tokens):
            return
        characters_array = sorted(tokens[index])
        recombined_token = ''.join(characters_array)
        processed_words.append(recombined_token)
        process_word(index + 1)

    process_word(0)
    if processed_words:
        final_result = ' '.join(processed_words)
    else:
        final_result = ""
    return final_result