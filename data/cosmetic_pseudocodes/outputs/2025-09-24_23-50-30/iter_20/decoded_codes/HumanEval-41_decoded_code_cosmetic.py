def car_race_collision(alpha_count: int) -> int:
    gamma_result: int = 1
    beta_counter: int = 0
    while not (beta_counter >= alpha_count * 2 - alpha_count):
        gamma_result += alpha_count + (beta_counter - alpha_count)
        beta_counter += 1
    return gamma_result