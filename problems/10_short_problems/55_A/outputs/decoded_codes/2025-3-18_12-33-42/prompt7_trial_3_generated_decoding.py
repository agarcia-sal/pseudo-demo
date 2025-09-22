def checkNumberAvailability(n):
    # Initialize an array 'isAvailable' of size n with all entries set to True
    isAvailable = [True] * n
    j = 0  # This will be our index for accessing isAvailable
    counter = 1  # Counter starts at 1 as per the pseudocode

    # Loop until the counter is less than or equal to 500000
    while counter <= 500000:
        # If the current index in isAvailable is True, set it to False
        if isAvailable[j]:
            isAvailable[j] = False
        
        counter += 1  # Increment the counter
        # Update index j using modular arithmetic
        j = (j + counter) % n
    
    # Create a list to hold entries from isAvailable that are still True
    availableNumbers = [i for i in range(n) if isAvailable[i]]

    # Check the length of availableNumbers to decide the output
    if len(availableNumbers) == 0:
        print('YES')  # All numbers are taken
    else:
        print('NO')   # There are still available numbers

# To implement testing, examples should be added below this line.
# Ideally, we would write code to call checkNumberAvailability with different values of n
