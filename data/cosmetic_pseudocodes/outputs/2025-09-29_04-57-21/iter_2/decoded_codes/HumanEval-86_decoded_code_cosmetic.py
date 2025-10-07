from typing import List

def anti_shuffle(input_string: str) -> str:
    words_array: List[str] = input_string.split(" ")
    rearranged_words: List[str] = []
    counter: int = 0

    while counter < len(words_array):
        current_word: str = words_array[counter]
        char_array: List[str] = list(current_word)
        swapped: bool = True

        while swapped:
            swapped = False
            for i in range(len(char_array) - 1):
                if char_array[i] > char_array[i + 1]:
                    char_array[i], char_array[i + 1] = char_array[i + 1], char_array[i]
                    swapped = True

        assembled_word: str = "".join(ch for ch in char_array)
        rearranged_words.append(assembled_word)
        counter += 1

    output_string: str = ""
    for pos in range(len(rearranged_words)):
        output_string += rearranged_words[pos]
        if pos < len(rearranged_words) - 1:
            output_string += " "

    return output_string