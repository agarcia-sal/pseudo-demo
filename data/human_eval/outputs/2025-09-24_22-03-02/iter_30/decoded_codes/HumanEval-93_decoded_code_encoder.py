def encode(message) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    index = 0
    length_of_vowels = len(vowels)
    while index < length_of_vowels:
        current_char = vowels[index]
        ascii_value = ord(current_char)
        replaced_char_code = ascii_value + 2
        replaced_char = chr(replaced_char_code)
        vowels_replace[current_char] = replaced_char
        index += 1
    swapped_message = message.swapcase()
    result_list = []
    message_length = len(swapped_message)
    i = 0
    while i < message_length:
        current_char = swapped_message[i]
        if current_char in vowels:
            result_list.append(vowels_replace[current_char])
        else:
            result_list.append(current_char)
        i += 1
    result_string = ""
    j = 0
    result_list_length = len(result_list)
    while j < result_list_length:
        result_string += result_list[j]
        j += 1
    return result_string