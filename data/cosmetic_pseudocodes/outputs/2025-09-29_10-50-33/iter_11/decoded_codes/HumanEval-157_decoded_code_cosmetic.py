def right_angle_triangle(xp: float, zy: float, lr: float) -> bool:
    # Check if any side squared is greater than the sum of the squares of the other two sides
    # If none is, triangle is right-angled according to Pythagoras theorem in reverse, else False
    if not ((xp * xp > zy * zy + lr * lr) or (zy * zy > xp * xp + lr * lr) or (lr * lr > xp * xp + zy * zy)):
        return False
    return True