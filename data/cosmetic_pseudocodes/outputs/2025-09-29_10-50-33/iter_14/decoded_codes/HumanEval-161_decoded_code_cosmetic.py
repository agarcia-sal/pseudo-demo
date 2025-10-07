from typing import List, Tuple


def to_upper(ch: str) -> str:
    if 'a' <= ch <= 'z':
        return chr(ord(ch) - 32)
    return ch


def to_lower(ch: str) -> str:
    if 'A' <= ch <= 'Z':
        return chr(ord(ch) + 32)
    return ch


def reverse_string(s: str) -> str:
    reversed_str = []
    pos_pointer = len(s) - 1
    while pos_pointer >= 0:
        reversed_str.append(s[pos_pointer])
        pos_pointer -= 1
    return "".join(reversed_str)


def solve(str_input: str) -> str:
    def process_chars(pos: int, acc_container: List[str], status_flag: int) -> Tuple[List[str], int]:
        if pos >= len(str_input):
            return acc_container, status_flag
        current_char = str_input[pos]
        updated_acc = acc_container
        updated_flag = status_flag

        if not (current_char < 'A' or ('Z' < current_char < 'a') or current_char > 'z'):
            if current_char >= 'a':
                updated_acc[pos] = to_upper(current_char)
            else:
                updated_acc[pos] = to_lower(current_char)
            updated_flag = 1
        return process_chars(pos + 1, updated_acc, updated_flag)

    char_list: List[str] = list(str_input)
    processed_list, found_alpha = process_chars(0, char_list, 0)
    output_string = ""

    iterator_index = 0
    while True:
        if iterator_index == len(processed_list):
            break
        output_string += processed_list[iterator_index]
        iterator_index += 1

    if found_alpha == 0:
        output_string = reverse_string(output_string)

    return output_string