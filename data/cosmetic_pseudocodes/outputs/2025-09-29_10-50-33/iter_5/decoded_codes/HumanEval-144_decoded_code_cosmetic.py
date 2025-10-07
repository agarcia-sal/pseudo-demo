from typing import Union

def simplify(fraction_a: str, fraction_b: str) -> bool:
    parts_a = fraction_a.split("/")
    parts_b = fraction_b.split("/")
    numerator_a: int = int(parts_a[0])
    denominator_a: int = int(parts_a[1])
    numerator_b: int = int(parts_b[0])
    denominator_b: int = int(parts_b[1])

    combined_numerator: int = numerator_a * numerator_b
    combined_denominator: int = denominator_a * denominator_b

    # Check if combined fraction is an integer
    division_result: float = combined_numerator / combined_denominator
    integer_part: int = int(division_result)

    if division_result != integer_part:
        return False
    return True