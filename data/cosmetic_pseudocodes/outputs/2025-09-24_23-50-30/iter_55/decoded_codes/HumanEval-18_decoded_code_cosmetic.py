from typing import Union

def how_many_times(alpha_input: Union[str, bytes], beta_token: Union[str, bytes]) -> int:
    gamma_counter: int = 0
    delta_limit: int = len(alpha_input) - len(beta_token)
    epsilon_index: int = 0

    while epsilon_index <= delta_limit:
        if alpha_input[epsilon_index : epsilon_index + len(beta_token)] == beta_token:
            gamma_counter += 1
        epsilon_index += 1

    return gamma_counter