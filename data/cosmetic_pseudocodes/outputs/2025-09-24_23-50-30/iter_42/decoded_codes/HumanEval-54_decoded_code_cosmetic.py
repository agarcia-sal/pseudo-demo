def same_chars(text_alpha: str, text_beta: str) -> bool:
    unique_alpha: set[str] = set(text_alpha)
    unique_beta: set[str] = set(text_beta)
    return unique_alpha == unique_beta