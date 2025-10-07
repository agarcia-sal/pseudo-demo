def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix = ""
    index = 0
    while index < beginning_of_suffix:
        prefix += string[index]
        index += 1
    reversed_prefix = ""
    index = len(prefix) - 1
    while index >= 0:
        reversed_prefix += prefix[index]
        index -= 1
    return string + reversed_prefix

def reverse_string(string: str) -> str:
    reversed_string = ""
    index = len(string) - 1
    while index >= 0:
        reversed_string += string[index]
        index -= 1
    return reversed_string