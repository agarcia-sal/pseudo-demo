def main():
    # Read an integer n from user input
    n = int(input())

    # Initialize a list of size n with all elements set to True
    isNotDeleted = [True] * n

    # Set initial variables
    currentIndex = 0
    i = 1

    # Loop while i is less than or equal to 500000
    while i <= 500000:
        # If the element at isNotDeleted[currentIndex] is True
        if isNotDeleted[currentIndex]:
            # Mark it as deleted
            isNotDeleted[currentIndex] = False
            
        # Increment i by 1
        i += 1
        
        # Update currentIndex to be (currentIndex + i) modulo n
        currentIndex = (currentIndex + i) % n

    # Create a new list with all elements from isNotDeleted that are still True
    remainingTrue = [x for x in isNotDeleted if x]

    # Determine output based on remaining values
    if len(remainingTrue) == 0:
        print('YES')  # Print 'YES' if no elements remain
    else:
        print('NO')   # Print 'NO' if there are elements remaining

# Execute the main function
if __name__ == "__main__":
    main()
