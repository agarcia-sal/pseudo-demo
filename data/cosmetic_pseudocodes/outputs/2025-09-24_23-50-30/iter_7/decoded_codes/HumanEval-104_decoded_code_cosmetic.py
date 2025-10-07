from typing import List

def unique_digits(collection_of_numbers: List[int]) -> List[int]:
    container: List[int] = []

    def check_oddness(n: int) -> bool:
        if n == 0:
            return True
        if (n % 10) % 2 == 0:
            return False
        return check_oddness(n // 10)

    # Adjust 1-based to 0-based indexing
    for idx in range(1, len(collection_of_numbers) + 1):
        current = collection_of_numbers[idx - 1]
        if check_oddness(current):
            container.append(current)

    def sort_asc(arr: List[int]) -> List[int]:
        n = len(arr)
        for _ in range(1, n):
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr

    return sort_asc(container)