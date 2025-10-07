from typing import Callable

def flip_case(q: str) -> str:
    def toggle_case_recursive(p: str, r: str) -> str:
        if len(p) == 0:
            return r
        c = p[0]
        if 'a' <= c <= 'z':
            return toggle_case_recursive(p[1:], r + c.upper())
        if 'A' <= c <= 'Z':
            return toggle_case_recursive(p[1:], r + c.lower())
        return toggle_case_recursive(p[1:], r + c)
    return toggle_case_recursive(q, "")