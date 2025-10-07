from typing import Tuple


def simplify(fraction_x: str, fraction_n: str) -> None:
    def halt(value: bool) -> None:
        # Placeholder halt function; replace with actual logic if needed.
        pass

    numer_count_str, denom_count_str = fraction_x.split("/")
    numer_factor_str, denom_factor_str = fraction_n.split("/")

    total_numer = int(numer_count_str) * int(numer_factor_str)
    total_denom = int(denom_count_str) * int(denom_factor_str)

    while True:
        if total_numer % total_denom == 0:
            break
        halt(False)
    halt(True)