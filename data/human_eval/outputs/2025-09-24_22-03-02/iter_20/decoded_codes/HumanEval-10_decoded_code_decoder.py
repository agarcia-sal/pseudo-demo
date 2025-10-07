def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)


def reverse_string(input_string: str) -> str:
    result = ''
    index = len(input_string) - 1
    while index >= 0:
        result += input_string[index]
        index -= 1
    return result


def make_palindrome(string: str) -> str:
    if string == '':
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix = string[:beginning_of_suffix]
    reversed_prefix = reverse_string(prefix)
    return string + reversed_prefix