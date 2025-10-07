from typing import List, Optional, Tuple

def find_closest_elements(Delta: List[float]) -> Optional[Tuple[float, float]]:
    def Inner(i: int, j: int, Closest: Optional[Tuple[float, float]], MinDist: Optional[float]) -> Optional[Tuple[float, float]]:
        if i >= len(Delta):
            return Closest
        if j >= len(Delta):
            return Inner(i + 1, 0, Closest, MinDist)
        if i != j:
            Diff = abs(Delta[i] - Delta[j])
            if MinDist is None or Diff < MinDist:
                NewClosest = (Delta[i], Delta[j]) if Delta[i] < Delta[j] else (Delta[j], Delta[i])
                return Inner(i, j + 1, NewClosest, Diff)
            return Inner(i, j + 1, Closest, MinDist)
        return Inner(i, j + 1, Closest, MinDist)
    return Inner(0, 0, None, None)