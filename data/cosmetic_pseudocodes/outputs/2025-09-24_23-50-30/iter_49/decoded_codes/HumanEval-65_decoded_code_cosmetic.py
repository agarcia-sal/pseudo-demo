from typing import Callable


def circular_shift(integer_x: int, integer_shift: int) -> str:
    def helper_function(latent_num: str, latent_step: int) -> str:
        if latent_step > len(latent_num):
            return latent_num[::-1]  # reverse string
        else:
            latent_boundary = len(latent_num) - latent_step
            return latent_num[latent_boundary:] + latent_num[:latent_boundary]

    return helper_function(str(integer_x), integer_shift)