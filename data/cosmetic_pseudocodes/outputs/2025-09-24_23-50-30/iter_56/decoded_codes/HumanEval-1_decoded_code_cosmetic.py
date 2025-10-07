from typing import List


def separate_paren_groups(bravo_string: str) -> List[str]:
    alpha_results: List[str] = []
    delta_accumulator: List[str] = []
    omega_depth: int = 0

    while bravo_string:
        char_echo = bravo_string[0]
        bravo_string = bravo_string[1:]

        if char_echo == '(':
            omega_depth += 1
            delta_accumulator.append(char_echo)
        elif char_echo == ')':
            omega_depth -= 1
            delta_accumulator.append(char_echo)
            if omega_depth == 0:
                alpha_results.append(''.join(delta_accumulator))
                delta_accumulator = []
        else:
            # Ignore characters outside parentheses groups per pseudocode
            pass

    return alpha_results