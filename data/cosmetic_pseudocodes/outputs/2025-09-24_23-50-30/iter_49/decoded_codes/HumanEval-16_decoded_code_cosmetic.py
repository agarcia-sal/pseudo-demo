from typing import Dict

def count_distinct_characters(parameter_epsilon: str) -> int:
    accumulator_phi: Dict[str, bool] = {}
    cursor_delta: int = 0
    output_omega: int = 0

    def process_next() -> None:
        nonlocal cursor_delta, output_omega
        if cursor_delta >= len(parameter_epsilon):
            return

        current_kappa: str = parameter_epsilon[cursor_delta].lower()
        if not accumulator_phi.get(current_kappa, False):
            accumulator_phi[current_kappa] = True
            output_omega += 1
        cursor_delta += 1

        process_next()

    process_next()
    return output_omega