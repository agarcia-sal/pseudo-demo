from typing import Dict

def encode(message: str) -> str:
    vowel_set: str = "AEIOUaeiou"
    shift_map: Dict[str, str] = {v: chr(ord(v) + 2) for v in vowel_set}

    swapped_message = []
    for char in message:
        if char.isupper():
            swapped_message.append(char.lower())
        elif char.islower():
            swapped_message.append(char.upper())
        else:
            swapped_message.append(char)
    swapped_message_str = "".join(swapped_message)

    result_chars = []
    index_counter = 0
    length = len(swapped_message_str)
    while index_counter < length:
        current_char = swapped_message_str[index_counter]
        if current_char in vowel_set and current_char in shift_map:
            result_chars.append(shift_map[current_char])
        else:
            result_chars.append(current_char)
        index_counter += 1

    return "".join(result_chars)