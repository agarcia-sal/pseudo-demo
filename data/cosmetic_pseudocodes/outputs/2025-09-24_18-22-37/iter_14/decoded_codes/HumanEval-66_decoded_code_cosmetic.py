def digitSum(circular_haze: str) -> int:
    if circular_haze == "":
        return 0

    temporary_sum: int = 0
    length_of_input: int = len(circular_haze)
    index_counter: int = 0

    while index_counter < length_of_input:
        current_element: str = circular_haze[index_counter]
        check_uppercase: bool = 'A' <= current_element <= 'Z'

        if check_uppercase:
            temporary_sum += ord(current_element)

        index_counter += 1

    return temporary_sum