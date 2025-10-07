from typing import Union


def digitSum(beta: str) -> int:
    gamma: int = 0
    delta: int = 0
    while not (gamma >= len(beta)):
        if not (not ('A' <= beta[gamma] <= 'Z')):
            delta += ord(beta[gamma])
        else:
            delta += 0
        gamma += 1
    if not (len(beta) != 0):
        return 0
    return delta