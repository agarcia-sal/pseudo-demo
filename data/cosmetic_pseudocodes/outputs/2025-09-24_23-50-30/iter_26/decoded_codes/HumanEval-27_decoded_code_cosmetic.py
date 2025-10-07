def flip_case(parameter_alpha: str) -> str:
    result_beta: str = ""
    index_gamma: int = 0
    while index_gamma < len(parameter_alpha):
        char_delta = parameter_alpha[index_gamma]
        if 'a' <= char_delta <= 'z':
            result_beta += char_delta.upper()
        elif 'A' <= char_delta <= 'Z':
            result_beta += char_delta.lower()
        else:
            result_beta += char_delta
        index_gamma += 1
    return result_beta