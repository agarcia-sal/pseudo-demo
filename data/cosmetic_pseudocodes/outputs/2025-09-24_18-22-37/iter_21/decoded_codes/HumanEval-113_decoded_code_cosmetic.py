from typing import List


def odd_count(array_of_words: List[str]) -> List[str]:
    result_sequence: List[str] = []
    index: int = 0
    while True:
        if index >= len(array_of_words):
            break
        current_word: str = array_of_words[index]
        counter: int = 0
        position: int = 0
        while True:
            if position >= len(current_word):
                break
            current_char: str = current_word[position]
            numeric_value: int = int(current_char)
            remainder: int = numeric_value % 2
            if remainder == 1:
                counter += 1
            position += 1
        temp_string: str = "the number of odd elements "
        temp_string += str(counter)
        temp_string += "n the str"
        temp_string += str(counter)
        temp_string += "ng "
        temp_string += str(counter)
        temp_string += " of the "
        temp_string += str(counter)
        temp_string += "nput."
        result_sequence.append(temp_string)
        index += 1
    return result_sequence