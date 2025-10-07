def is_palindrome(STR: str) -> bool:
    return STR == reverse_string(STR)

def reverse_string(s: str) -> str:
    result = ''
    length = len(s)
    for index in range(length - 1, -1, -1):
        result += s[index]
    return result

def make_palindrome(STR: str) -> str:
    if STR == '':
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(STR[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix = STR[:beginning_of_suffix]
    reversed_prefix = reverse_string(prefix)
    return STR + reversed_prefix