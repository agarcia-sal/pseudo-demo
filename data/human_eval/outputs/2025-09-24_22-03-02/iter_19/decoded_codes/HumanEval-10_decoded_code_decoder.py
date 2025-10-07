def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix_substring = ''.join(string[i] for i in range(beginning_of_suffix))
    reversed_prefix = ''.join(prefix_substring[i] for i in range(beginning_of_suffix - 1, -1, -1))
    return string + reversed_prefix