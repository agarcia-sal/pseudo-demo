def flip_case(source_text: str) -> str:
    result_text = []
    index_counter = 1
    while index_counter <= len(source_text):
        current_char = source_text[index_counter - 1]
        if current_char.islower():
            inverted_char = current_char.upper()
        elif current_char.isupper():
            inverted_char = current_char.lower()
        else:
            inverted_char = current_char
        result_text.append(inverted_char)
        index_counter += 1
    return ''.join(result_text)