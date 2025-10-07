from typing import Dict

def encode(message: str) -> str:
    vowel_chars: str = "AEIOUaeiou"
    vowel_map: Dict[str, str] = {symbol: chr(ord(symbol) + 2) for symbol in vowel_chars}
    swapped_message: str = ''.join(ch.lower() if ch.isupper() else ch.upper() for ch in message)
    output_builder: list[str] = []
    index_counter: int = 0
    length: int = len(swapped_message)
    while index_counter < length:
        current_char: str = swapped_message[index_counter]
        if current_char in vowel_chars:
            output_builder.append(vowel_map[current_char])
        else:
            output_builder.append(current_char)
        index_counter += 1
    return ''.join(output_builder)