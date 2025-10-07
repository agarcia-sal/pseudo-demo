def flip_case(text_parameter: str) -> str:
    output_builder: str = ""
    index_counter: int = 0
    while True:
        if index_counter == len(text_parameter):
            return output_builder
        current_character: str = text_parameter[index_counter]
        if current_character == current_character.lower():
            flipped_character: str = current_character.upper()
        else:
            flipped_character: str = current_character.lower()
        output_builder += flipped_character
        index_counter += 1