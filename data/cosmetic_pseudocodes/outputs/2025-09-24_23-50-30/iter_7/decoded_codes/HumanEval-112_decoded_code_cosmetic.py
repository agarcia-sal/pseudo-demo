from typing import List, Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def remove_chars(index_i: int, acc_list: List[str]) -> List[str]:
        if index_i >= len(string_s):
            return acc_list
        if string_s[index_i] not in string_c:
            return remove_chars(index_i + 1, acc_list + [string_s[index_i]])
        else:
            return remove_chars(index_i + 1, acc_list)

    filtered_chars = remove_chars(0, [])
    filtered_string = ''.join(filtered_chars)

    is_palindrome = True
    left_index = 0
    right_index = len(filtered_string) - 1
    while left_index <= right_index:
        if filtered_string[left_index] != filtered_string[right_index]:
            is_palindrome = False
            break
        left_index += 1
        right_index -= 1

    return filtered_string, is_palindrome