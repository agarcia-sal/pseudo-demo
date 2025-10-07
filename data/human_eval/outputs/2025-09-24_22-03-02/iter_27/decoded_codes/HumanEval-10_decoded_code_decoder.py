def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(substring(string, beginning_of_suffix, len(string))):
        beginning_of_suffix += 1
    prefix = substring(string, 0, beginning_of_suffix)
    reversed_prefix = reverse_string(prefix)
    return string + reversed_prefix

def substring(input_string: str, start_index: int, end_index: int) -> str:
    result = ""
    index = start_index
    while index < len(input_string) and index < end_index:
        result += input_string[index]
        index += 1
    return result

def reverse_string(input_string: str) -> str:
    result = ""
    index = len(input_string) - 1
    while index >= 0:
        result += input_string[index]
        index -= 1
    return result