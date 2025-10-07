def right_angle_triangle(side_one: float, side_two: float, side_three: float) -> bool:
    square_first = side_one * side_one
    square_second = side_two * side_two
    square_third = side_three * side_three

    if square_first == square_second + square_third:
        return True
    elif square_second == square_first + square_third:
        return True
    elif square_third == square_first + square_second:
        return True
    else:
        return False