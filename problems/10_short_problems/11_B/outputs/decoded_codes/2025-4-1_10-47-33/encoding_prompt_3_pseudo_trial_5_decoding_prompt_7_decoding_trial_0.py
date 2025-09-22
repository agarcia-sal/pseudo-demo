# Begin implementation of the pseudocode

# Step 1: Read an integer input from the user and convert to absolute value
userInput = abs(int(input()))  # Get user input and convert to absolute integer
index = 0  # Initialize index variable

# Step 2: Infinite loop to find the required index
while True:
    # Calculate the sum of the first 'index' natural numbers
    sum = (index * (index + 1)) // 2  # Using integer division to calculate the sum

    # Calculate the difference from the user input
    difference = sum - userInput  # Calculate the difference

    # Step 3: Check if we found the desired sum
    if sum == userInput:
        print(index)  # Print the index if sum matches user input
        break  # Exit the loop as the desired sum is found

    # Step 4: If sum is greater than user input
    elif sum > userInput:
        # Step 5: Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print the index if the difference is even
            break  # Exit the loop as the conditions are fulfilled

    # Step 6: Increment index for the next iteration
    index += 1  # Increase the index by 1 for the next iteration
