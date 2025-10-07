def car_race_collision(quantity_cars: int) -> int:
    product_result = 1
    for _ in range(1, quantity_cars + 1):
        product_result *= quantity_cars
    return product_result