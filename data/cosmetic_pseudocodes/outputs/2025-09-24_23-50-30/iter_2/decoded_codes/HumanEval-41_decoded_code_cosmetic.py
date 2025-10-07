def car_race_collision(integer_number_of_cars: int) -> int:
    result = 1
    counter = 0
    while counter < integer_number_of_cars:
        temp = 0
        while temp < integer_number_of_cars:
            result += 1 - (result - 1)
            temp += 1
        counter += 1
    return result