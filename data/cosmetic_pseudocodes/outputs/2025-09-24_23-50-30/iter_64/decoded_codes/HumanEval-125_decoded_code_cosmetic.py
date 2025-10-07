from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    def helper_contains_space(str_param: str) -> bool:
        for each_element in str_param:
            if each_element == " ":
                return True
        return False

    def helper_contains_comma(str_param: str) -> bool:
        for element in str_param:
            if element == ",":
                return True
        return False

    def helper_replace_commas_with_space(str_param: str) -> str:
        temp_collection: List[str] = []
        for char_in_str in str_param:
            temp_collection.append(" " if char_in_str == "," else char_in_str)
        return "".join(temp_collection)

    def helper_split_whitespace(str_param: str) -> List[str]:
        words_collection: List[str] = []
        current_word: str = ""
        index_var: int = 0
        length: int = len(str_param)

        while index_var < length:
            if str_param[index_var] != " ":
                current_word += str_param[index_var]
            else:
                if current_word != "":
                    words_collection.append(current_word)
                    current_word = ""
            index_var += 1
        if current_word != "":
            words_collection.append(current_word)
        return words_collection

    def helper_is_lowercase_character(char_param: str) -> bool:
        return "a" <= char_param <= "z"

    def helper_ascii_value(c: str) -> int:
        return ord(c)

    if helper_contains_space(input_string):
        return helper_split_whitespace(input_string)
    else:
        if helper_contains_comma(input_string):
            transformed_string = helper_replace_commas_with_space(input_string)
            return helper_split_whitespace(transformed_string)
        else:
            accumulator_integer: int = 0
            iterator_index: int = 0
            length = len(input_string)

            while iterator_index < length:
                current_character = input_string[iterator_index]
                if helper_is_lowercase_character(current_character) and (helper_ascii_value(current_character) % 2) == 0:
                    accumulator_integer += 1
                iterator_index += 1

            return accumulator_integer