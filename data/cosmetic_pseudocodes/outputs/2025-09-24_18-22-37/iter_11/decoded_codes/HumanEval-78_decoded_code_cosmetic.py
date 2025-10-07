def hex_key(str_input: str) -> int:
    primes_collection = {'2', '3', '5', '7', 'B', 'D'}
    prime_count_accumulator = 0
    current_position = 0
    last_position = len(str_input) - 1
    while current_position <= last_position:
        current_char = str_input[current_position]
        if current_char in primes_collection:
            prime_count_accumulator += 1
        else:
            dummy_var = 0  # explicitly retained from pseudocode
        current_position += 1
    return prime_count_accumulator