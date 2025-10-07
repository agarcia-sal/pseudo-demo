from typing import List


def anti_shuffle(token_line: str) -> str:
    words_collection: List[str] = []
    cursor: int = 0
    length: int = len(token_line)

    # Extract words separated by spaces
    while cursor < length:
        start_idx = cursor
        while cursor < length and token_line[cursor] != ' ':
            cursor += 1
        words_collection.append(token_line[start_idx:cursor])
        cursor += 1  # skip the space

    reordered_terms: List[str] = []

    def process_word(index: int) -> None:
        if index == len(words_collection):
            return
        current_chunk = words_collection[index]
        char_box: List[str] = [ch for ch in current_chunk]

        # Sort characters in char_box using bubble sort style
        position_a = 0
        while position_a < len(char_box) - 1:
            position_b = position_a + 1
            while position_b < len(char_box):
                if char_box[position_a] > char_box[position_b]:
                    char_box[position_a], char_box[position_b] = char_box[position_b], char_box[position_a]
                position_b += 1
            position_a += 1

        reconstructed_word = ''.join(char_box)
        reordered_terms.append(reconstructed_word)
        process_word(index + 1)

    process_word(0)

    final_phrase: str = ' '.join(reordered_terms)
    return final_phrase