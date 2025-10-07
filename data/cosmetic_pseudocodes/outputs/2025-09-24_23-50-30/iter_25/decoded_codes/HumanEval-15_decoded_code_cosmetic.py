from typing import List

def string_sequence(integer_n: int) -> str:
    def helper(counter: int, accumulator: List[str]) -> List[str]:
        if counter > integer_n:
            return accumulator
        return helper(counter + 1, accumulator + [str(counter)])

    string_list: List[str] = helper(0, [])
    result_string: str = ""
    for item in string_list:
        if not result_string:
            result_string = item
        else:
            result_string += " " + item
    return result_string