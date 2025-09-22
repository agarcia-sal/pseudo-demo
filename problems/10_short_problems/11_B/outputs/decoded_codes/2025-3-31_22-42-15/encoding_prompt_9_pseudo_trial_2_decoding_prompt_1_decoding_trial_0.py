# Step 1: Receive Input
targetNumber = abs(int(input()))

# Step 2: Initialize Variables
currentInteger = 0

# Step 3: Start an Infinite Loop
while True:
    # Step 4: Calculate Triangular Number
    triangularNumber = (currentInteger * (currentInteger + 1)) / 2
    
    # Step 5: Determine the Difference
    difference = triangularNumber - targetNumber
    
    # Step 6: Check Conditions
    if triangularNumber == targetNumber:
        # Output currentInteger
        print(currentInteger)
        break  # Exit the loop (valid number found)
    
    elif triangularNumber > targetNumber:
        # Check if difference is an even number
        if difference % 2 == 0:
            # Output currentInteger
            print(currentInteger)
            break  # Exit the loop (valid adjustment found)

    # Step 7: Increment the Integer
    currentInteger += 1
