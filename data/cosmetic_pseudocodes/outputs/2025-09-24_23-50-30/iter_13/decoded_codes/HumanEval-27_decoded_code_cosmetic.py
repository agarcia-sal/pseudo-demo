def flip_case(source_text: str) -> str:
    output_builder: list[str] = []
    for current_char in source_text:
        if 'a' <= current_char <= 'z':
            output_builder.append(current_char.upper())
        elif 'A' <= current_char <= 'Z':
            output_builder.append(current_char.lower())
        else:
            output_builder.append(current_char)
    return ''.join(output_builder)