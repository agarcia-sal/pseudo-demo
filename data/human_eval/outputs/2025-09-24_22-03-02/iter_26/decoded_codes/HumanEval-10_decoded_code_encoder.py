def is_palindrome(string: str) -> bool:
    return string == reverse_of_string(string)

def make_palindrome(string: str) -> str:
    if string == '':
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    prefix_substring = substring_of_string(0, beginning_of_suffix - 1, string)
    reversed_prefix = reverse_of_string(prefix_substring)
    result_string = string + reversed_prefix
    return result_string

def reverse_of_string(input_string: str) -> str:
    character_list = []
    for index in range(len(input_string) - 1, -1, -1):
        character_list.append(input_string[index])
    reversed_string = concatenate_list_of_characters(character_list)
    return reversed_string

def substring_of_string(start_index: int, end_index: int, input_string: str) -> str:
    character_list = []
    for index in range(start_index, end_index + 1):
        character_list.append(input_string[index])
    substring = concatenate_list_of_characters(character_list)
    return substring

def concatenate_list_of_characters(character_list: list) -> str:
    result_string = ''
    for index in range(len(character_list)):
        result_string += character_list[index]
    return result_string