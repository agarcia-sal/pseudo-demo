def main():
    # Step 1: Set up input
    n = int(input())  # Read an integer n from user input

    # Step 2: Initialize a list of True values
    isNotDeleted = [True] * n  # Create a list of size n with all elements set to True

    # Step 3: Set initial variables
    currentIndex = 0  # Starting index
    i = 1  # Start with 1 for incrementing

    # Step 4: Loop through the range while updating the list
    while i <= 500000:
        # Check if the current index hasn't been marked as deleted
        if isNotDeleted[currentIndex]:
            isNotDeleted[currentIndex] = False  # Mark the current index as deleted
        
        i += 1  # Increment i
        currentIndex = (currentIndex + i) % n  # Update currentIndex, ensuring wrapping around with modulo

    # Step 5: Check for remaining True values
    remainingTrue = [value for value in isNotDeleted if value]  # Create a list of remaining True values

    # Step 6: Determine output based on remaining values
    if len(remainingTrue) == 0:
        print('YES')  # No remaining True values
    else:
        print('NO')  # There are remaining True values

# Run the main function to execute the program
if __name__ == "__main__":
    main()
