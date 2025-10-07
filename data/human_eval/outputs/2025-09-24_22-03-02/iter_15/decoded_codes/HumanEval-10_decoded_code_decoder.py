def is_palindrome(string: str) -> bool:
    return string == reverse_string(string)

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix_to_append = reverse_string(string[:beginning_of_suffix])
    return string + prefix_to_append

def reverse_string(string: str) -> str:
    reversed_string = ""
    for index in range(len(string) - 1, -1, -1):
        reversed_string += string[index]
    return reversed_string