from typing import List, Union


def split_words(input_string: str) -> Union[int, List[str]]:
    def tail_recursive_function(index: int, result_string: str) -> str:
        if index >= len(input_string):
            return result_string
        else:
            return tail_recursive_function(index + 1, result_string + input_string[index])

    if ' ' not in input_string:
        if ',' not in input_string:
            filtered_chars: List[str] = []
            for pos in range(len(input_string)):
                ch = input_string[pos]
                if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0:
                    filtered_chars.append(ch)
            total_count = len(filtered_chars)
            return total_count
        else:
            replaced_string = ''.join(' ' if c == ',' else c for c in input_string)
            split_result: List[str] = []
            word_buffer = ""
            for char in replaced_string:
                if char != ' ':
                    word_buffer += char
                elif len(word_buffer) > 0:
                    split_result.append(word_buffer)
                    word_buffer = ""
            if len(word_buffer) > 0:
                split_result.append(word_buffer)
            return split_result
    else:
        split_result: List[str] = []
        word_buffer = ""
        for char in input_string:
            if char != ' ':
                word_buffer += char
            elif len(word_buffer) > 0:
                split_result.append(word_buffer)
                word_buffer = ""
        if len(word_buffer) > 0:
            split_result.append(word_buffer)
        return split_result