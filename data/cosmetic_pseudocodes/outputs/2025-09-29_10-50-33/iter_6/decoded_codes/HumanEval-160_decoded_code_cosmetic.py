from typing import List, Union, Any
import operator

def do_algebra(commands_array: List[str], values_array: List[Any]) -> Any:
    formula_text: str = str(values_array[0])

    def append_terms(index: int) -> None:
        if index >= len(commands_array):
            return
        current_command: str = commands_array[index]
        current_value: Any = values_array[index]
        nonlocal formula_text
        formula_text += current_command + str(current_value)
        append_terms(index + 1)

    append_terms(1)

    # Using eval with restricted globals for safety; 
    # assumes formula_text is a valid algebraic expression.
    return eval(formula_text, {"__builtins__": {}})