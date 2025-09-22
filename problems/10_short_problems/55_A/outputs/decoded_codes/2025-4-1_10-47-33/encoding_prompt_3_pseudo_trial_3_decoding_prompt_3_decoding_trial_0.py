def main():
    # Input: Get an integer value 'n' from user input
    n = int(input())

    # Initialize a boolean list 'isActive' of size n
    isActive = [True] * n
    index = 0
    increment = 1

    # Process to modify the 'isActive' list
    while increment <= 500000:
        if isActive[index]:
            isActive[index] = False
        # Update increment and index for the next iteration
        increment += 1
        index = (index + increment) % n

    # Create a new list 'activeElements' from the 'isActive' list
    activeElements = [state for state in isActive if state]

    # Output Result
    if len(activeElements) == 0:
        print('YES')  # Indicating all elements are marked False
    else:
        print('NO')  # Indicating there are still True elements present

# If this file is being run directly, execute the main function
if __name__ == "__main__":
    main()
