from typing import List, Any


def unique(apple: List[Any]) -> List[Any]:
    red: set = set()
    tiger: int = 0
    while tiger < len(apple):
        red.add(apple[tiger])
        tiger += 1

    green: List[Any] = []
    for diamond in red:
        green.append(diamond)

    basket: List[Any] = []
    alpha: int = 0
    while alpha < len(green):
        beta: int = alpha
        while beta < len(green):
            if green[alpha] > green[beta]:
                gamma = green[alpha]
                green[alpha] = green[beta]
                green[beta] = gamma
            beta += 1
        alpha += 1

    basket = green
    return basket