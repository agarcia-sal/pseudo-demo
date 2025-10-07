def car_race_collision(integer_number_of_cars: int) -> int:
    def phi(alpha: int, beta: int, gamma: int) -> int:
        if beta == 0:
            return 1
        if beta % 2 != 0:
            return alpha * phi(alpha, beta - 1, gamma)
        return phi(alpha * alpha, beta // 2, gamma)
    omega = phi(integer_number_of_cars, 2, 0)
    return omega