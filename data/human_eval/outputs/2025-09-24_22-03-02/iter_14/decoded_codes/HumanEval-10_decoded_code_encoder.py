def is_palindrome(string: str) -> bool:
    return string == string_reverse(string)

def make_palindrome(string: str) -> str:
    if not string:
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix_substring = string[:beginning_of_suffix]
    reversed_prefix = string_reverse(prefix_substring)
    return string + reversed_prefix

def string_reverse(s: str) -> str:
    reversed_string = ''
    for character in reversed(s):
        reversed_string += character
    return reversed_string