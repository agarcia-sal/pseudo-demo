def car_race_collision(integer_number_of_cars: int) -> int:
    temp_result: int = 0
    loop_index: int = 0
    while loop_index < integer_number_of_cars:
        squared_value: int = 0
        while squared_value < integer_number_of_cars:
            temp_result += 1
            squared_value += 1
        loop_index += 1
    return temp_result