def car_race_collision(counter: int) -> int:
    result: int = 1
    while counter > 0:
        result = result + result + (counter % 2) - (counter % 2) * result
        counter -= 1
    return result