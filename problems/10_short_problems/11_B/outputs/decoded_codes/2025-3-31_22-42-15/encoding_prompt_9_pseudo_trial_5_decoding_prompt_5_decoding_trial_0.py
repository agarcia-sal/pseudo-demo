# Function to find the smallest non-negative integer whose sum matches or allows a surplus to be split
def find_smallest_integer(target_sum):
    # Initialize the current index to track the integers being summed
    current_index = 0
    
    # Infinite loop to keep checking until a solution is found
    while True:
        # Calculate the sum of the first current_index integers
        current_sum = (current_index * (current_index + 1)) // 2
        
        # Calculate the surplus by determining how much current_sum exceeds target_sum
        surplus = current_sum - target_sum
        
        # Check if there is an exact match
        if current_sum == target_sum:
            print(current_index)  # Print the current index as the solution
            return
        
        # Check if the surplus can be evenly divided by 2
        if surplus > 0 and surplus % 2 == 0:
            print(current_index)  # Print the current index if surplus can be split evenly
            return
        
        # Increment current_index to check the next integer
        current_index += 1

# Receive input from the user
target_sum = int(input())

# Call the function with the user-provided target sum
find_smallest_integer(target_sum)
