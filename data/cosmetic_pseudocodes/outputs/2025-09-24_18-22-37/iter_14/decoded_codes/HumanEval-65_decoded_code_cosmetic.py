def circular_shift(alpha_num: int, beta_num: int) -> str:
    sigma_string = str(alpha_num)
    if beta_num > len(sigma_string):
        # Return the reverse of the string
        return sigma_string[::-1]
    else:
        kappa = len(sigma_string)
        lambda_start = kappa - beta_num
        # Extract right part from lambda_start to end
        mu_right_part = sigma_string[lambda_start:kappa]
        # Extract left part from start to lambda_start
        nu_left_part = sigma_string[:lambda_start]
        return mu_right_part + nu_left_part