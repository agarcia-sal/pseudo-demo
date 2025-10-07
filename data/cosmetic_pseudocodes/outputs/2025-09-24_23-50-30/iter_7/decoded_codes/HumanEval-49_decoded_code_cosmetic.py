def modp(int_alpha: int, int_beta: int) -> int:
    acc: int = 1
    counter: int = 0
    while counter < int_alpha:
        doubled = acc * 2
        acc = doubled - (doubled // int_beta) * int_beta
        counter += 1
    return acc