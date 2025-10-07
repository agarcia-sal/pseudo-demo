def encode_shift(s: str) -> str:
    encoded_characters = []
    index = 0
    while index < len(s):
        ch = s[index]
        shifted_value = ((ord(ch) + 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_value)
        encoded_characters.append(shifted_char)
        index += 1
    encoded_string = ""
    index = 0
    while index < len(encoded_characters):
        encoded_string += encoded_characters[index]
        index += 1
    return encoded_string

def decode_shift(s: str) -> str:
    decoded_characters = []
    index = 0
    while index < len(s):
        ch = s[index]
        shifted_value = ((ord(ch) - 5 - ord("a")) % 26) + ord("a")
        shifted_char = chr(shifted_value)
        decoded_characters.append(shifted_char)
        index += 1
    decoded_string = ""
    index = 0
    while index < len(decoded_characters):
        decoded_string += decoded_characters[index]
        index += 1
    return decoded_string