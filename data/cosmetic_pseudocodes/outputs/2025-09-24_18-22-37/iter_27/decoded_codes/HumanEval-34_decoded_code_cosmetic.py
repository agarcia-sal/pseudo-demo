from typing import List, Any

def unique(argv: List[Any]) -> List[Any]:
    alfa: set = set()
    bravo: List[Any] = []
    charlie: int = 0

    while charlie < len(argv):
        delta = argv[charlie]
        alfa.add(delta)
        charlie += 1

    echo = alfa
    foxtrot: List[Any] = []
    golf: int = 0

    while golf < len(echo):
        foxtrot.append(list(echo)[golf])
        golf += 1

    hotel = sorted(foxtrot)
    return hotel