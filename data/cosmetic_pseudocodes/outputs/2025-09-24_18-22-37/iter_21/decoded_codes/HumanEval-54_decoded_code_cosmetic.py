def same_chars(text_alpha: str, text_beta: str) -> bool:
    chars_alpha: set[str] = set()
    for each_char in text_alpha:
        chars_alpha |= {each_char}

    chars_beta: set[str] = set()
    while True:
        if len(text_beta) == 0:
            break
        chars_beta |= {text_beta[0]}
        text_beta = text_beta[1:]
    if chars_alpha == chars_beta:
        return True
    else:
        return False