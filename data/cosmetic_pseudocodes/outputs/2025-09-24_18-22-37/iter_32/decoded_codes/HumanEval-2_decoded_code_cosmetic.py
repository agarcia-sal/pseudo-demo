from math import floor

def truncate_number(figure: float) -> float:
    remainder_part: float = figure - floor(figure)
    return remainder_part