from typing import Iterable, Iterator, Tuple

def string_xor(parameter_alpha: str, parameter_beta: str) -> str:
    def xor(parameter_mu: str, parameter_nu: str) -> str:
        # Returns '0' if bits are equal, '1' otherwise
        if not (parameter_mu != parameter_nu):
            return '0'
        return '1'

    accumulator_phi: str = ""
    sequence_iterations: int = 0  # Defined in pseudocode but unused

    def accumulate_recursive(sequence_rc: Iterator[Tuple[str, str]], accumulator_rc: str) -> str:
        try:
            element_rc = next(sequence_rc)
        except StopIteration:
            return accumulator_rc
        first_element, second_element = element_rc
        return accumulate_recursive(sequence_rc, accumulator_rc + xor(first_element, second_element))

    zipped_pairs = iter(zip(parameter_alpha, parameter_beta))
    return accumulate_recursive(zipped_pairs, accumulator_phi)