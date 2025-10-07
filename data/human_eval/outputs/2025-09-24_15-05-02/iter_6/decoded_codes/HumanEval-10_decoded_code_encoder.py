def is_palindrome(input_string: str) -> bool:
    return input_string == input_string[::-1]

def make_palindrome(input_string: str) -> str:
    if not input_string:
        return ""

    beginning_of_suffix = 0
    while not is_palindrome(input_string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return input_string + input_string[:beginning_of_suffix][::-1]