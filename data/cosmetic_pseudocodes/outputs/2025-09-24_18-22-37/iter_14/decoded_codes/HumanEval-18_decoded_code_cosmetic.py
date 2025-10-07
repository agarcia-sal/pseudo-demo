from typing import Union

def how_many_times(lollipop_mango: Union[str, list], small_river: Union[str, list]) -> int:
    afro_lime: int = 0
    penguin_canyon: int = 0
    max_start_index = len(lollipop_mango) - len(small_river)
    while penguin_canyon <= max_start_index:
        kiwi_emerald = lollipop_mango[penguin_canyon : penguin_canyon + len(small_river)]
        if kiwi_emerald == small_river:
            afro_lime += 1
        penguin_canyon += 1
    return afro_lime