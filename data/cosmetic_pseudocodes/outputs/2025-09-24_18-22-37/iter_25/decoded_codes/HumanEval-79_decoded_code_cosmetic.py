def decimal_to_binary(alpha_num: int) -> str:
    gamma_bin_rep: str = ""
    beta_str: str = ""
    delta_first_char: str = ""

    epsilon_temp_num: int = alpha_num

    while epsilon_temp_num > 1:
        gamma_bin_rep = str(epsilon_temp_num % 2) + gamma_bin_rep
        epsilon_temp_num //= 2

    gamma_bin_rep = str(epsilon_temp_num) + gamma_bin_rep

    delta_first_char = "b"
    beta_str = delta_first_char + gamma_bin_rep + delta_first_char

    return beta_str