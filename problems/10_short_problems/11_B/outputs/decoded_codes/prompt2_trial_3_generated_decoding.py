# Step 1: Accept a number from user input and ensure it is a non-negative integer.
absoluteValue = int(input())
if absoluteValue < 0:
    raise ValueError("Input must be a non-negative integer.")

# Step 2: Initialize index to 0.
index = 0

# Step 3: Enter an infinite loop to find a solution.
while True:
    # Calculate sum of the first 'index' natural numbers.
    sumOfIndex = index * (index + 1) // 2
    
    # Calculate the difference.
    difference = sumOfIndex - absoluteValue
    
    # Step 4: Check conditions for valid solutions.
    if sumOfIndex == absoluteValue:
        print(index)  # Output the index if sumOfIndex equals absoluteValue.
        break  # Exit loop.
        
    if sumOfIndex > absoluteValue:
        # Check if the difference is an even number.
        if difference % 2 == 0:
            print(index)  # Output the index if the difference is even.
            break  # Exit loop.
    
    # Step 5: Increment index by 1 for the next iteration.
    index += 1

# Step 6: End of program execution after finding a solution.
