def flip_case(parameter_one: str) -> str:
    result_container = []
    for element in parameter_one:
        transformed_char = element.upper() if 'a' <= element <= 'z' else element.lower()
        result_container.append(transformed_char)
    return ''.join(result_container)