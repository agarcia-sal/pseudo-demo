from typing import List

def flip_case(parameter_string: str) -> str:
    length_counter: int = len(parameter_string)
    result_buffer: List[str] = []
    index_iter: int = 0

    while index_iter < length_counter:
        current_char: str = parameter_string[index_iter]
        if not ('a' <= current_char <= 'z'):
            if 'A' <= current_char <= 'Z':
                # convert uppercase to lowercase by adding 32 to ASCII
                result_buffer.append(chr(ord(current_char) + 32))
            else:
                result_buffer.append(current_char)
        else:
            # convert lowercase to uppercase by subtracting 32 from ASCII
            result_buffer.append(chr(ord(current_char) - 32))
        index_iter += 1

    final_string: str = ''.join(result_buffer)
    return final_string