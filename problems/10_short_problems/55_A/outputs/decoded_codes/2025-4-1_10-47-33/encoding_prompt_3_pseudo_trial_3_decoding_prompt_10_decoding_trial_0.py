def main():
    # Input
    n = int(input())  # Get an integer value 'n' from user input

    # Initialize a boolean list 'isActive' of size n
    is_active = [True] * n
    index = 0
    increment = 1

    # Process to modify the 'isActive' list
    while increment <= 500000:
        if is_active[index]:
            is_active[index] = False  # Mark this index as inactive
        # Update increment and index for the next iteration
        increment += 1
        index = (index + increment) % n  # Circular increment

    # Create a new list 'active_elements' from the 'isActive' list
    active_elements = [status for status in is_active if status]

    # Output Result
    if len(active_elements) == 0:
        print('YES')  # Indicating all elements are marked False
    else:
        print('NO')  # Indicating there are still True elements present

if __name__ == "__main__":
    main()
