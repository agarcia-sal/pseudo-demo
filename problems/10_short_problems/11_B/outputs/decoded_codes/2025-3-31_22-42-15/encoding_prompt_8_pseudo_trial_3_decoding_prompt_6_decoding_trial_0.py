# Start the Program

# Get User Input
target_value = int(input())  # Read an integer value from the user
target_value = abs(target_value)  # Calculate the absolute value of target_value

# Initialize Variables
current_index = 0  # Set a counter variable to 0

# Begin Infinite Loop
while True:
    # Calculate the sum of the first 'current_index' integers
    sum_of_integers = (current_index * (current_index + 1)) // 2  # Use integer division

    # Calculate the difference between sum_of_integers and target_value
    difference = sum_of_integers - target_value

    # Check Conditions
    if sum_of_integers == target_value:
        print(current_index)  # Print current_index if it equals target_value
        break  # Exit the loop
    
    if sum_of_integers > target_value:
        if difference % 2 == 0:  # Check if the difference is evenly divisible by 2
            print(current_index)  # Print current_index when the condition is met
            break  # Exit the loop
    
    # Increment current_index by 1 to check the next integer
    current_index += 1
