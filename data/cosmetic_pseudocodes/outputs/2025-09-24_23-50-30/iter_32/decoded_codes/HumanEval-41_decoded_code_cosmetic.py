def car_race_collision(binding_counter: int) -> int:
    binding_result: int = 1
    counter_flag: int = binding_counter
    while counter_flag > 0:
        binding_result *= binding_counter
        counter_flag -= 1
    return binding_result