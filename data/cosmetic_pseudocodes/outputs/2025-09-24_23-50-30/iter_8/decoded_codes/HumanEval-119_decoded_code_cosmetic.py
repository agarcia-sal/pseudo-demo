from typing import List

def match_parens(input_array: List[str]) -> str:
    def verify(input_string: str) -> bool:
        count = 0
        for symbol in input_string:
            if symbol == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    first_appended = input_array[0] + input_array[1]
    second_appended = input_array[1] + input_array[0]
    if verify(first_appended) or verify(second_appended):
        return 'Yes'
    else:
        return 'No'