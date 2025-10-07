def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def reverse_string(input_string: str) -> str:
    length = len(input_string)
    reversed_string = ""
    index = length - 1
    while index >= 0:
        reversed_string += input_string[index]
        index -= 1
    return reversed_string

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(substring(string, beginning_of_suffix, len(string) - 1)):
        beginning_of_suffix += 1
    prefix_substring = substring(string, 0, beginning_of_suffix - 1)
    reversed_prefix = reverse_string(prefix_substring)
    return string + reversed_prefix

def substring(text: str, start_index: int, end_index: int) -> str:
    result = ""
    index = start_index
    while index <= end_index:
        result += text[index]
        index += 1
    return result