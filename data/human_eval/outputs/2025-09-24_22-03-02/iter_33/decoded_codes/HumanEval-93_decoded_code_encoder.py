def encode(message) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels_replace = {}
    index = 0
    while index < len(vowels):
        i = vowels[index]
        ascii_value = ord(i)
        ascii_value_plus_two = ascii_value + 2
        replacement_char = chr(ascii_value_plus_two)
        vowels_replace[i] = replacement_char
        index += 1
    swapped_message = message.swapcase()
    result_list = []
    index = 0
    while index < len(swapped_message):
        i = swapped_message[index]
        if i in vowels:
            character = vowels_replace[i]
        else:
            character = i
        result_list.append(character)
        index += 1
    result = ""
    index = 0
    while index < len(result_list):
        result += result_list[index]
        index += 1
    return result