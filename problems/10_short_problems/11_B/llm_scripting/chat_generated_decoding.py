def minimum_steps_to_reach_target(n: int) -> int:
    """
    Finds the minimum number of steps (i) required to reach the position n on a number line,
    moving in increments 1, 2, 3, ..., i with the possibility to flip the direction of any move.
    
    Args:
        n (int): Target position (can be positive or negative).
        
    Returns:
        int: Minimum number of steps needed.
    """
    n = abs(n)  # Only the distance matters, direction can be flipped
    i = 0

    while True:
        # Calculate the i-th triangular number: sum of first i natural numbers
        triangular_sum = (i * (i + 1)) // 2
        
        # Difference between current triangular sum and target
        difference = triangular_sum - n
        
        if triangular_sum == n:
            # Exact match found
            return i
        elif triangular_sum > n and difference % 2 == 0:
            # We can correct by flipping some steps because difference is even
            return i
            
        i += 1

        
if __name__ == "__main__":
    target = abs(int(input("Enter the target number: ")))  # Ensure input is an integer
    steps = minimum_steps_to_reach_target(target)
    print(steps)
