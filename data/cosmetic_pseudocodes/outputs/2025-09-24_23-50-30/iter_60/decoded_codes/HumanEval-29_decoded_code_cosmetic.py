from typing import List, Optional, Any


def filter_by_prefix(a: List[str], b: str) -> List[str]:
    def recursion(c: Optional[Any], d: List[str], e: List[str]) -> List[str]:
        if not d:
            return list(reversed(e))
        if d[0].startswith(b):
            return recursion(c, d[1:], [d[0]] + e)
        return recursion(c, d[1:], e)

    return recursion(None, a, [])