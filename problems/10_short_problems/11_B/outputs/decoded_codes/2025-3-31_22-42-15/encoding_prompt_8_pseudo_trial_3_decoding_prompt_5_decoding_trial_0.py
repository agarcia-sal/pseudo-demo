# Start the Program

# Get User Input
target_value = int(input())  # Read an integer value from the user
target_value = abs(target_value)  # Calculate the absolute value of targetValue

# Initialize Variables
current_index = 0  # Set a counter variable to 0

# Begin Infinite Loop
while True:
    # Calculate the sum of the first 'currentIndex' integers
    sum_of_integers = (current_index * (current_index + 1)) // 2
    
    # Calculate the difference between sumOfIntegers and targetValue
    difference = sum_of_integers - target_value
    
    # Check Conditions
    if sum_of_integers == target_value:
        print(current_index)  # Print currentIndex
        break  # Exit the loop
    elif sum_of_integers > target_value:
        # Check if difference is evenly divisible by 2
        if difference % 2 == 0:
            print(current_index)  # Print currentIndex
            break  # Exit the loop
    
    # Increment currentIndex by 1 for the next iteration
    current_index += 1
