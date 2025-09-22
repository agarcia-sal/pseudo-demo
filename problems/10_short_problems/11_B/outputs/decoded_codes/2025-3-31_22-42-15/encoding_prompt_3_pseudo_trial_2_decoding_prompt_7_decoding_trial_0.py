# Start of the program

# Step 1: Get user input
inputNumber = abs(int(input()))  # Read an integer input and take its absolute value

# Step 2: Initialize loop variable
index = 0  # Start from the first natural number

# Step 3: Begin an infinite loop to find the solution
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2  # Use integer division for accuracy
    
    # Calculate the difference between the sum and inputNumber
    difference = sum - inputNumber

    # Step 4: Check if the current sum equals the input number
    if sum == inputNumber:
        print(index)  # Print the index when the sum equals the input number
        break  # Exit the loop

    # Step 5: Check if the current sum exceeds the input number
    elif sum > inputNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the index when the difference is even
            break  # Exit the loop
    
    # Increment the loop variable
    index += 1  # Move to the next index to continue the search

# End of the program
