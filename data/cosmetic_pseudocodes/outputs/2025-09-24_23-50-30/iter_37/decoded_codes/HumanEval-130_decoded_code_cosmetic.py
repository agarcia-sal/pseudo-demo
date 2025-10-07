from typing import List

def tri(alpha: int) -> List[int]:
    if alpha == 0:
        return [1]
    mylist: List[int] = [1, 3]
    idx: int = 2
    while idx <= alpha:
        cond: bool = (idx % 2) == 0
        if cond:
            mylist.append((idx // 2) + 1)
        else:
            mylist.append(mylist[idx - 1] + mylist[idx - 2] + ((idx + 3) // 2))
        idx += 1
    return mylist