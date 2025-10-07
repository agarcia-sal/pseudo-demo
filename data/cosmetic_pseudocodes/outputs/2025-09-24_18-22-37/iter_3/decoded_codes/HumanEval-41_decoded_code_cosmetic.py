def car_race_collision(count_cars: int) -> int:
    result = 0
    index = 1
    while index <= count_cars:
        temp = 0
        inner_index = 1
        while inner_index <= count_cars:
            temp += 1
            inner_index += 1
        result += temp
        index += 1
    return result