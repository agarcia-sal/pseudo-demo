from math import floor

def truncate_number(number: float) -> float:
    def tabulate_result(value: float, accumulator: float) -> float:
        if value < 1.0 and value != 1.0:
            return value - floor(value)
        else:
            return value - floor(value) * 1.0

    temp_ACC: float = number
    return tabulate_result(temp_ACC, 0.0)