def encode(message: str) -> str:
    vowels = "aeiouAEIOU"
    vowels_replace = {}
    for index in range(len(vowels)):
        i = vowels[index]
        char_code = ord(i)
        new_char_code = char_code + 2
        new_char = chr(new_char_code)
        vowels_replace[i] = new_char
    message = message.swapcase()
    result_chars = []
    for index in range(len(message)):
        i = message[index]
        if i in vowels:
            result_chars.append(vowels_replace[i])
        else:
            result_chars.append(i)
    result = ""
    for index in range(len(result_chars)):
        result += result_chars[index]
    return result