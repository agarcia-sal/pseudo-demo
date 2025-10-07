def encode(message) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = []
    for index in range(len(vowels)):
        key = vowels[index]
        value = chr(ord(key) + 2)
        vowels_replace.append((key, value))
    vowels_replace = dict(vowels_replace)
    message = message.swapcase()
    result_list = []
    for index in range(len(message)):
        current_char = message[index]
        if current_char in vowels_replace:
            result_list.append(vowels_replace[current_char])
        else:
            result_list.append(current_char)
    result_string = "".join(result_list)
    return result_string