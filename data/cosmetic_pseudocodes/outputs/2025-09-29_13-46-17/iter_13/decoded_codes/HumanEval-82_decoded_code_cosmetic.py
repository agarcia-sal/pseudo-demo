from typing import Callable


def prime_length(input_string: str) -> bool:
    def quxₓ(state_x: int) -> bool:
        if state_x not in (0, 1):
            def plr(ξ: int, α: int) -> bool:
                if ξ >= α:
                    return True

                def ygn() -> bool:
                    # If length_of_string is divisible by ξ, return False, else recurse with ξ+1
                    if (length_of_string % ξ) == 0:
                        return False
                    else:
                        return plr(ξ + 1, α)

                return ygn()

            length_of_string = len(input_string)
            return plr(2, length_of_string)
        else:
            return False

    return quxₓ(len(input_string))