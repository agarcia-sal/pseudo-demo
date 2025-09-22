# Step 1: Start the program
# (No explicit action needed in Python)

# Step 2: Read an integer value from user input
targetValue = abs(int(input()))  # Step 2 - Reading input and storing absolute value

# Step 3: Initialize a variable index to 0
index = 0

# Step 4: Enter an infinite loop
while True:
    # Calculate the triangular number
    triangularNumber = (index * (index + 1)) // 2  # Using integer division
    
    # Calculate the difference
    difference = triangularNumber - targetValue
    
    # Check conditions
    if triangularNumber == targetValue:
        print(index)  # Print the current index
        break  # Exit the loop
    elif triangularNumber > targetValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the current index
            break  # Exit the loop
    
    # Increment index by 1 to check the next triangular number
    index += 1

# Step 5: End the program
# (No explicit action needed in Python)
