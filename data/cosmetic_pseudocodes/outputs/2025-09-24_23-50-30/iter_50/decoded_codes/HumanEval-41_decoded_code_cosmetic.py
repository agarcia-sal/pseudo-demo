def car_race_collision(x_count: int) -> int:
    y_total: int = 0
    z_index: int = 0
    while z_index < x_count:
        y_total += x_count
        z_index += 1
    return y_total