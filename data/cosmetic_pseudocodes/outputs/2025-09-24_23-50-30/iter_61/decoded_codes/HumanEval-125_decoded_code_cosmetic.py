from typing import List, Union


def split_words(alpha: str) -> Union[List[str], int]:
    contains_space: bool = ' ' in alpha
    contains_comma: bool = ',' in alpha

    def recursive_split(list_chars: List[str], acc: str) -> List[str]:
        if not list_chars:
            return [acc] if acc else []
        head, *tail = list_chars
        if head in {' ', '\t', '\n'}:
            if not acc:
                return [] + recursive_split(tail, "")
            else:
                return [acc] + recursive_split(tail, "")
        else:
            return recursive_split(tail, acc + head)

    def split_string(textual: str) -> List[str]:
        res = recursive_split(list(textual), "")
        return [element for element in res if len(element) > 0]

    if contains_space:
        return split_string(alpha)
    elif contains_comma:
        replaced_list = [' ' if char == ',' else char for char in alpha]
        replaced_string = ''.join(replaced_list)
        return split_string(replaced_string)
    else:
        def to_numeric(c: str) -> int:
            return ord(c)

        def is_lower_even(c: str) -> bool:
            return 'a' <= c <= 'z' and (to_numeric(c) % 2) == 0

        chars_list = list(alpha)
        filtered_chars = [c for c in chars_list if is_lower_even(c)]
        result_length = len(filtered_chars)
        return result_length