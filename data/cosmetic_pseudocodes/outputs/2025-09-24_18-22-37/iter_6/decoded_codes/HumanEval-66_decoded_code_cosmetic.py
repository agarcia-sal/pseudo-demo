def digitSum(text_data: str) -> int:
    result_count: int = 0
    index_counter: int = 0
    if text_data != "":
        while index_counter < len(text_data):
            current_element: str = text_data[index_counter]
            if "A" <= current_element <= "Z":
                character_code: int = ord(current_element)
                result_count += character_code
            else:
                result_count += 0
            index_counter += 1
        return result_count
    return 0