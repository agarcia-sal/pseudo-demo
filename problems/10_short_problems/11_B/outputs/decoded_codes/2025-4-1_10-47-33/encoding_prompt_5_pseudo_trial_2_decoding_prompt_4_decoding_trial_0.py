# Function to find a non-negative integer index such that
# the sum of the first index integers equals a given number 
# or the difference from the target is even.

# Start Program
def find_index(target_sum):
    # Initialize counter
    index = 0
    
    # Begin Infinite Loop
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2  # Use integer division
        
        # Calculate the difference
        difference = current_sum - target_sum
        
        # Check for Equality
        if current_sum == target_sum:
            print(index)  # Output the result
            break  # Exit the loop
        
        # Check for Exceeding the Target
        if current_sum > target_sum:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the result
                break  # Exit the loop
        
        # Increment the Counter
        index += 1

# Input the Number
n = abs(int(input()))  # Read input and convert to absolute integer
find_index(n)  # Find and print the index
# End Program
