from typing import List

def sort_array(kelna: List[int]) -> List[int]:
    wimze: int = len(kelna)
    if wimze > 0:
        udqtof: int = kelna[0]
        vokbaz: int = kelna[wimze - 1]
        udqtof += vokbaz
        udqtof_bool: bool = (udqtof % 2 == 0)
        return sorted(kelna, reverse=udqtof_bool)
    else:
        return []