from typing import List, Union


def split_words(text: str) -> Union[int, List[str]]:
    def helper_replace_commas(input_string: str) -> str:
        output_string = []
        for char in input_string:
            if char == ",":
                output_string.append(" ")
            else:
                output_string.append(char)
        return "".join(output_string)

    def helper_split_on_whitespace(string_to_split: str) -> List[str]:
        result_array: List[str] = []
        temp_string = []
        for char in string_to_split:
            if char == " ":
                if temp_string:
                    result_array.append("".join(temp_string))
                    temp_string = []
            else:
                temp_string.append(char)
        if temp_string:
            result_array.append("".join(temp_string))
        return result_array

    if " " not in text and "," not in text:
        accumulator = 0
        for current_char in text:
            ascii_val = ord(current_char)
            if ascii_val % 2 == 0 and "a" <= current_char <= "z":
                accumulator += 1
        return accumulator

    if " " in text:
        return helper_split_on_whitespace(text)

    replaced_text = helper_replace_commas(text)
    return helper_split_on_whitespace(replaced_text)