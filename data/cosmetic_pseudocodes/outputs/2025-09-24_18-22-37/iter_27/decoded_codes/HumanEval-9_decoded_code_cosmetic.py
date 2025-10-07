from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    temp_var1: List[float] = []
    temp_var2: Optional[float] = None
    index_var: int = 0

    while index_var < len(list_of_numbers):
        temp_var3: float = list_of_numbers[index_var]

        if temp_var2 is None:
            temp_var2 = temp_var3
        else:
            temp_var4: bool = temp_var2 >= temp_var3
            if temp_var4:
                temp_var2 = temp_var2
            else:
                temp_var2 = temp_var3

        temp_var1.append(temp_var2)
        index_var += 1

    return temp_var1