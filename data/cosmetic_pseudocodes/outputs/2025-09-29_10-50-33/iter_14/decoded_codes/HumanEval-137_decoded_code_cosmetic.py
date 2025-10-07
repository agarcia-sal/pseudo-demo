from typing import Union, Optional


def compare_one(a: Union[str, object], b: Union[str, object]) -> Optional[Union[str, object]]:
    def substitute_commas(input_value: Union[str, object]) -> Union[str, object]:
        if isinstance(input_value, str):
            result_collection = []
            for character in input_value:
                char_substitute = '.' if character == ',' else character
                result_collection.append(char_substitute)
            return ''.join(result_collection)
        else:
            return input_value

    transformed_a = substitute_commas(a)
    transformed_b = substitute_commas(b)

    lhs_value = float(transformed_a)
    rhs_value = float(transformed_b)

    if lhs_value == rhs_value:
        return None
    if lhs_value > rhs_value:
        return a
    else:
        return b