from typing import List, TypeVar, Callable, Sequence

T = TypeVar('T')

def monotonic(list_of_elements: Sequence[T]) -> bool:
    # Helper lambda to check if for each element x, 
    # lambda(x) equals either min or max of all elements under lambda,
    # meaning all elements map to the same min or max value (non-decreasing or non-increasing)
    # For monotonicity by identity, lambda is identity
    identity: Callable[[T], T] = lambda x: x

    def check(func: Callable[[T], T]) -> bool:
        mapped = list(map(func, list_of_elements))
        min_val = min(mapped)
        max_val = max(mapped)
        return all((mapped[i] == mapped[i] and (mapped[i] == min_val or mapped[i] == max_val)) for i in range(len(mapped)))

    # According to pseudocode logic, check if elements are sorted either ascending or descending
    # But the pseudocode uses a lambda that checks if lambda(x) == min or max of lambda(list_of_elements)
    # Actually the pseudocode looks like:
    # For each element y: (min(y) and lambda(y)==min) or (lambda(y)==min(reversed))
    # Interpreted as the list is monotonic (either non-decreasing or non-increasing)
    # We'll test directly if list_of_elements is sorted ascending or descending

    # Using Python's built-in comparisons for monotonic check is clearer and efficient:
    if all(list_of_elements[i] <= list_of_elements[i+1] for i in range(len(list_of_elements)-1)):
        return True
    if all(list_of_elements[i] >= list_of_elements[i+1] for i in range(len(list_of_elements)-1)):
        return True
    return False