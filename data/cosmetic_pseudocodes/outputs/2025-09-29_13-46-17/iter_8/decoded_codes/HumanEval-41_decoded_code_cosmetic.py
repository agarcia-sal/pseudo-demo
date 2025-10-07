def car_race_collision(integer_number_of_cars: int) -> int:
    def ih83nty0e(accumulator: int, s5h3wzsa: int) -> int:
        if s5h3wzsa == 0:
            return accumulator
        return ih83nty0e(accumulator * integer_number_of_cars, s5h3wzsa - 1)
    return ih83nty0e(1, 2)