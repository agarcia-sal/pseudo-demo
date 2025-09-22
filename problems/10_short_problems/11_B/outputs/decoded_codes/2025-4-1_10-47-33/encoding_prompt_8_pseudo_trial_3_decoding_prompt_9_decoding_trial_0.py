# Function to find the smallest non-negative integer based on the target number provided by the user.
def find_smallest_integer():
    # Set the target number as the absolute value of the input.
    target_number = abs(int(input()))
    index = 0  # Initialize the index to 0

    # Start an infinite loop
    while True:
        # Calculate the sum of all integers from 0 to index
        sum_to_index = (index * (index + 1)) // 2  # Use integer division for precision

        # Calculate the difference between sum_to_index and target_number
        difference = sum_to_index - target_number  

        # Check for exact match
        if sum_to_index == target_number:
            print(index)  # Print the index if it matches
            break  # Exit the loop

        # Check for exceeding value
        if sum_to_index > target_number:  
            if difference % 2 == 0:  # Check if the difference is even
                print(index)  # Print the index if the difference is even
                break  # Exit the loop

        # Increment index to continue searching
        index += 1  

# Call the function to execute the logic
find_smallest_integer()
