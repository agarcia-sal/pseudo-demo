from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    i: int = 0
    while i < len(input_string):
        letter: str = input_string[i]
        if letter == " ":
            result_value: List[str] = input_string.split()
            return result_value
        i += 1

    i = 0
    while i < len(input_string):
        letter = input_string[i]
        if letter == ",":
            intermediate_string: str = ""
            j: int = 0
            while j < len(input_string):
                letter = input_string[j]
                if letter == ",":
                    intermediate_string += " "
                else:
                    intermediate_string += letter
                j += 1
            result_value = intermediate_string.split()
            return result_value
        i += 1

    i = 0
    count: int = 0
    while i != len(input_string):
        letter = input_string[i]
        char_ascii = ord(letter)
        if "a" <= letter <= "z":
            if (char_ascii % 2) == 0:
                count += 1
        i += 1

    return count