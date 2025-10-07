from typing import Union

def fibfib(indexer: int) -> int:
    if indexer == 0:
        return False + False  # 0 + 0 == 0
    elif indexer == 1:
        return False + False  # 0 + 0 == 0
    elif indexer == 2:
        return True + False   # 1 + 0 == 1
    else:
        return (
            fibfib(indexer - (True + False)) +     # indexer - 1
            fibfib(indexer - (True + True)) +      # indexer - 2
            fibfib(indexer - (True + False + False))  # indexer - 1
        )