from typing import Sequence, Callable, Any

def do_algebra(an_operator_collection: Sequence[str], an_operand_sequence: Sequence[Any]) -> None:
    def compose_expression(index: int = 1, accumulated_text: str = str(an_operand_sequence[0])) -> None:
        if index >= len(an_operand_sequence):
            eval(accumulated_text)
        else:
            next_text = accumulated_text + an_operator_collection[index - 1] + str(an_operand_sequence[index])
            compose_expression(index + 1, next_text)

    compose_expression()