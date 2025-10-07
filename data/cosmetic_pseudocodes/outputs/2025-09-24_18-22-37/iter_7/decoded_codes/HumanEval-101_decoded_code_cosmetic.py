from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string:
        temp_list: List[str] = []
        index_counter: int = 0
        while index_counter < len(input_string):
            current_char: str = input_string[index_counter]
            if current_char != ',':
                temp_list.append(current_char)
            else:
                temp_list.append(' ')
            index_counter += 1

        combined_str: str = ''
        position: int = 0
        while position < len(temp_list):
            combined_str += temp_list[position]
            position += 1

        return combined_str.split()
    else:
        return []