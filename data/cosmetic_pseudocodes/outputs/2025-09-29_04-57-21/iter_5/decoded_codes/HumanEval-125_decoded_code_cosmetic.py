from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        # input_string contains at least one space
        words_collection: List[str] = []
        for element in input_string.split():
            words_collection.append(element)
        return words_collection
    elif "," in input_string:
        altered_input = ""
        for symbol in input_string:
            altered_input += " " if symbol == "," else symbol
        return altered_input.split()
    else:
        tally = 0
        index_pointer = 0
        length_of_input = len(input_string) - 1
        while index_pointer <= length_of_input:
            current_char = input_string[index_pointer]
            if "a" <= current_char <= "z":
                ascii_val = ord(current_char)
                if ascii_val % 2 == 0:
                    tally += 1
            index_pointer += 1
        return tally