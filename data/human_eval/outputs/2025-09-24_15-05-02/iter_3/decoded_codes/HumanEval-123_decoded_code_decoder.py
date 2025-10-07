def get_odd_collatz(n):
    """
    Generate a sorted list of odd numbers encountered in the Collatz sequence starting from n.

    Parameters:
    n (int): The starting integer of the Collatz sequence.

    Returns:
    List[int]: Sorted list of odd numbers from the Collatz sequence.
    """
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        if n % 2 == 1:
            odd_collatz.append(n)

    return sorted(odd_collatz)