def process_boolean_list():
    # Step 2: Receive Input
    n = int(input())  # Read the size of the list from the user

    # Step 3: Initialize List
    statusList = [True] * n  # Create a list of size n, all initialized to True

    # Step 4: Initialize Variables
    currentIndex = 0
    increment = 1

    # Step 5: Process List
    while increment <= 500000:
        # Check if the current index in statusList is True
        if statusList[currentIndex]:
            # Change that element in statusList to False
            statusList[currentIndex] = False
        
        increment += 1  # Increase increment by 1
        # Update the currentIndex using the formula
        currentIndex = (currentIndex + increment) % n  # Wrap around to stay within the list size

    # Step 6: Check Remaining Values
    remainingTrue = [status for status in statusList if status]  # Create a list of any remaining True values

    # Step 7: Generate Output
    if not remainingTrue:  # If remainingTrue is empty (all values are False)
        print("YES")
    else:
        print("NO")

# To run the function:
process_boolean_list()
