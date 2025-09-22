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
        # Output the currentInteger if it matches the targetNumber
        print(currentInteger)
        break  # Exit the loop (valid number found)
    
    elif triangularNumber > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            # Output the currentInteger if it can be adjusted by an even number
            print(currentInteger)
            break  # Exit the loop (valid adjustment found)
    
    # Step 7: Increment the Integer
    currentInteger += 1
