def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(substring_with_indices(string, beginning_of_suffix, len(string) - 1)):
        beginning_of_suffix += 1
    prefix_to_reverse = substring_with_indices(string, 0, beginning_of_suffix - 1)
    reversed_prefix = reverse_string(prefix_to_reverse)
    return string + reversed_prefix

def reverse_string(string: str) -> str:
    reversed_string = ""
    index = len(string) - 1
    while index >= 0:
        reversed_string += string[index]
        index -= 1
    return reversed_string

def substring_with_indices(string: str, start_index: int, end_index: int) -> str:
    result_string = ""
    current_index = start_index
    while current_index <= end_index:
        result_string += string[current_index]
        current_index += 1
    return result_string