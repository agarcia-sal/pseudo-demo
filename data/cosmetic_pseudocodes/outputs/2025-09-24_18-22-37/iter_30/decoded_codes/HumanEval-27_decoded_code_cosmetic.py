def flip_case(original_text: str) -> str:
    result_text = []
    idx = 0
    length = len(original_text)
    while idx < length:
        current_ch = original_text[idx]
        if 'a' <= current_ch <= 'z':
            inverted_ch = current_ch.upper()
        elif 'A' <= current_ch <= 'Z':
            inverted_ch = current_ch.lower()
        else:
            inverted_ch = current_ch
        result_text.append(inverted_ch)
        idx += 1
    return ''.join(result_text)