from typing import Callable

def flip_case(distinct_input: str) -> str:
    def loop_convert_case(index_counter: int, collection_result: str) -> str:
        if index_counter < len(distinct_input):
            ch = distinct_input[index_counter]
            if 'a' <= ch <= 'z':
                # Convert lowercase to uppercase by subtracting 32 from ASCII code
                return loop_convert_case(index_counter + 1, collection_result + chr(ord(ch) - 32))
            elif 'A' <= ch <= 'Z':
                # Convert uppercase to lowercase by adding 32 to ASCII code
                return loop_convert_case(index_counter + 1, collection_result + chr(ord(ch) + 32))
            else:
                return loop_convert_case(index_counter + 1, collection_result + ch)
        else:
            return collection_result

    return loop_convert_case(0, "")