from typing import Iterable, List

def unique_digits(sequence_of_numbers: Iterable[int]) -> List[int]:
    def digits_of(n: int) -> List[int]:
        # Extract digits of the number n
        return [int(d) for d in str(abs(n))]

    # Filter numbers where every digit is odd
    zeta = filter(
        lambda omega: all((psi % 2) == 1 for psi in digits_of(omega)),
        sequence_of_numbers
    )
    eta = sorted(zeta)
    return eta