def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix = string[:beginning_of_suffix]
    reversed_prefix = reverse_string(prefix)
    return string + reversed_prefix

def reverse_string(s: str) -> str:
    result = ""
    length = len(s)
    index = length - 1
    while index >= 0:
        result += s[index]
        index -= 1
    return result