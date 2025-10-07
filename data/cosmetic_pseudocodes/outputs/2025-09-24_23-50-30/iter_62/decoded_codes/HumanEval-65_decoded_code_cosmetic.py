def circular_shift(num_alpha: int, num_beta: int) -> str:
    text_gamma = str(num_alpha)
    if not (num_beta <= len(text_gamma)):
        return text_gamma[::-1]
    return text_gamma[-num_beta:] + text_gamma[:-num_beta]