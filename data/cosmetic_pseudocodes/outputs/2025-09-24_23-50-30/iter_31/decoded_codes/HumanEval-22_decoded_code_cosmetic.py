from typing import Iterable, List, Any


def filter_integers(omega: Iterable[Any]) -> List[int]:
    return [alpha for alpha in omega if isinstance(alpha, int)]