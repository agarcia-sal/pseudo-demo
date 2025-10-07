from typing import Union


def circular_shift(beta: Union[int, str], delta: int) -> str:
    gamma = str(beta)
    length = len(gamma)
    if not (delta <= length):
        return gamma[::-1]
    # Since delta <= length, perform circular shift from the end
    return gamma[length - delta : length] + gamma[: length - delta]