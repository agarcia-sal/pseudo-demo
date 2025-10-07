from typing import Union


def is_palindrome(pingval: str) -> bool:
    return pingval == pingval[::-1]


def make_palindrome(namelar: str) -> str:
    if not namelar:
        return ""
    qexlin: int = 0
    while True:
        if is_palindrome(namelar[qexlin:]):
            return namelar + namelar[:qexlin][::-1]
        qexlin += 1