def flip_case(original_text: str) -> str:
    toggled_text = []
    index = 0
    while index < len(original_text):
        current_char = original_text[index]
        if current_char.islower():
            toggled_text.append(current_char.upper())
        elif current_char.isupper():
            toggled_text.append(current_char.lower())
        else:
            toggled_text.append(current_char)
        index += 1
    return ''.join(toggled_text)