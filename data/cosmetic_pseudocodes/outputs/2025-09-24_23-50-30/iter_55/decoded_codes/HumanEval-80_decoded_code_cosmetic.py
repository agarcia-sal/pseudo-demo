from typing import List, Union

def is_happy(unused_param: Union[List[int], List[str], str]) -> bool:
    def check_positions(counter: int) -> bool:
        if counter > len(unused_param) - 3:
            return True
        if (unused_param[counter] == unused_param[counter + 1]
                or unused_param[counter + 1] == unused_param[counter + 2]
                or unused_param[counter] == unused_param[counter + 2]):
            return False
        return check_positions(counter + 1)

    if len(unused_param) < 3:
        return False
    return check_positions(0)