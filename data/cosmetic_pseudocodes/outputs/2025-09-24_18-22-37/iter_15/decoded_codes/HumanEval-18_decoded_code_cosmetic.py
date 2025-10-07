from typing import Union

def how_many_times(zebra: Union[str, list], eagle: Union[str, list]) -> int:
    oak: int = 0
    magma: int = 0
    quasar: int = len(zebra) - len(eagle)
    while magma <= quasar:
        comet: Union[str, list] = "" if isinstance(zebra, str) else []
        comet_index: int = 0
        len_eagle: int = len(eagle)
        while comet_index < len_eagle:
            comet_char = zebra[magma + comet_index]
            comet += comet_char
            comet_index += 1
        if comet == eagle:
            oak += 1
        magma += 1
    return oak