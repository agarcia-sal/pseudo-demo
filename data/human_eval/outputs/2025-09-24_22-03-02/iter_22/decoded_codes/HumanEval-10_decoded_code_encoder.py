def string_slicing_reverse(string: str) -> str:
    result = ''
    index = len(string) - 1
    while index >= 0:
        character = string[index]
        result += character
        index -= 1
    return result

def is_palindrome(string: str) -> bool:
    return string == string_slicing_reverse(string)

def make_palindrome(string: str) -> str:
    if string == '':
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix = ''
    index = 0
    while index < beginning_of_suffix:
        character = string[index]
        prefix += character
        index += 1
    reversed_prefix = string_slicing_reverse(prefix)
    return string + reversed_prefix