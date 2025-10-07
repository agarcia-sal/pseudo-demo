from typing import List

def match_parens(input_array: List[str]) -> str:
    def validate(expression: str) -> bool:
        counter: int = 0
        index: int = 0
        length: int = len(expression)
        while index < length:
            if expression[index] == '(':
                counter += 1
            else:
                counter -= 1
            if counter < 0:
                return False
            index += 1
        return counter == 0

    first_concat: str = input_array[0] + input_array[1]
    second_concat: str = input_array[1] + input_array[0]

    if validate(first_concat):
        return 'Yes'
    else:
        return 'Yes' if validate(second_concat) else 'No'