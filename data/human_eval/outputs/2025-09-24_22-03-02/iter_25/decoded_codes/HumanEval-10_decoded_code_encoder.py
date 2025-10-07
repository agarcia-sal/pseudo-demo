def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def reverse_string(string: str) -> str:
    result = ''
    length = len(string)
    for i in range(length - 1, -1, -1):
        result += string[i]
    return result

def make_palindrome(string: str) -> str:
    if string == '':
        return ''
    beginning_of_suffix = 0
    length = len(string)
    while True:
        substring = ''
        for j in range(beginning_of_suffix, length):
            substring += string[j]
        if is_palindrome(substring):
            break
        beginning_of_suffix += 1
    prefix = ''
    for k in range(beginning_of_suffix):
        prefix += string[k]
    reversed_prefix = reverse_string(prefix)
    return string + reversed_prefix