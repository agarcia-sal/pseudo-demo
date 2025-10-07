def is_palindrome(string: str) -> bool:
    reversed_string = ""
    index = len(string) - 1
    while index >= 0:
        reversed_string += string[index]
        index -= 1
    if string == reversed_string:
        return True
    else:
        return False

def make_palindrome(string: str) -> str:
    if string == "":
        return ""
    beginning_of_suffix = 0
    while True:
        substring = ""
        length_string = len(string)
        index_substring = beginning_of_suffix
        while index_substring < length_string:
            substring += string[index_substring]
            index_substring += 1
        palindrome_check = is_palindrome(substring)
        if palindrome_check == True:
            break
        else:
            beginning_of_suffix += 1
    prefix = ""
    index_prefix = 0
    while index_prefix < beginning_of_suffix:
        prefix += string[index_prefix]
        index_prefix += 1
    reversed_prefix = ""
    index_reversed = len(prefix) - 1
    while index_reversed >= 0:
        reversed_prefix += prefix[index_reversed]
        index_reversed -= 1
    return string + reversed_prefix