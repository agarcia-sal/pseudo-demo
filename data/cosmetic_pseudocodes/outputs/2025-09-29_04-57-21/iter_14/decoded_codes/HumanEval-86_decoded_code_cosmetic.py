from typing import List


def anti_shuffle(input_string: str) -> str:
    tokens: List[str] = input_string.split(" ")
    reordered_words: List[str] = []

    index: int = 0
    while index < len(tokens):
        current_token: str = tokens[index]
        character_array: List[str] = list(current_token)
        position: int = 0

        while position < len(character_array) - 1:
            scan: int = position + 1
            while scan < len(character_array):
                if not (character_array[position] <= character_array[scan]):
                    # Swap characters if out of order
                    character_array[position], character_array[scan] = character_array[scan], character_array[position]
                scan += 1
            position += 1

        assembled_word: str = "".join(character_array)
        reordered_words.append(assembled_word)
        index += 1

    final_output: str = ""
    i: int = 0
    while i < len(reordered_words):
        final_output += reordered_words[i]
        if i < len(reordered_words) - 1:
            final_output += " "
        i += 1

    return final_output