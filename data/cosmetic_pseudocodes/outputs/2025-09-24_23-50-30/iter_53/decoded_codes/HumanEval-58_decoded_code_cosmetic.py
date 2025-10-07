from typing import List, Set, TypeVar

T = TypeVar('T')

def common(lumbo: List[T], rhyth: List[T]) -> List[T]:
    def helper_fauna(robe: Set[T], milk: List[T], goat: Set[T]) -> Set[T]:
        if not milk:
            return goat
        else:
            def inner_loop(mutt: Set[T], rice: T, duck: List[T]) -> Set[T]:
                if not duck:
                    return mutt
                else:
                    if rice == duck[0]:
                        return inner_loop(mutt.union({rice}), rice, duck[1:])
                    else:
                        return inner_loop(mutt, rice, duck[1:])
            return helper_fauna(inner_loop(robe, robe and next(iter(robe)) or milk[0], milk), milk[1:], goat) if robe else helper_fauna(inner_loop(robe, milk[0], milk), milk[1:], goat)

    seed: Set[T] = helper_fauna(set(), lumbo, set())
    return sorted(seed)