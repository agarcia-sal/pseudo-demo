from typing import List

def flip_case(str_param: str) -> str:
    result_collection: List[str] = []
    idx_counter: int = 0

    while idx_counter < len(str_param):
        current_char: str = str_param[idx_counter]
        if 'a' <= current_char <= 'z':
            # convert lowercase to uppercase by offsetting ASCII code
            result_collection.append(chr(ord(current_char) - (ord('a') - ord('A'))))
        elif 'A' <= current_char <= 'Z':
            # convert uppercase to lowercase by offsetting ASCII code
            result_collection.append(chr(ord(current_char) + (ord('a') - ord('A'))))
        else:
            result_collection.append(current_char)

        idx_counter += 1

    return ''.join(result_collection)