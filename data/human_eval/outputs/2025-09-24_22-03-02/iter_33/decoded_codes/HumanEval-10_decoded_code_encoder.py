def is_palindrome(string: str) -> bool:
    reversed_string = ''
    length_of_string = len(string)
    for index in range(length_of_string - 1, -1, -1):
        reversed_string += string[index]
    if string == reversed_string:
        return True
    else:
        return False

def make_palindrome(string: str) -> str:
    if string == '':
        return ''

    beginning_of_suffix = 0
    while True:
        substring_to_check = ''
        length_of_string = len(string)
        for index in range(beginning_of_suffix, length_of_string):
            substring_to_check += string[index]

        result = is_palindrome(substring_to_check)
        if result:
            break
        else:
            beginning_of_suffix += 1

    prefix_to_reverse = ''
    for index in range(beginning_of_suffix):
        prefix_to_reverse += string[index]

    reversed_prefix = ''
    length_of_prefix = len(prefix_to_reverse)
    for index in range(length_of_prefix - 1, -1, -1):
        reversed_prefix += prefix_to_reverse[index]

    result_string = string + reversed_prefix
    return result_string