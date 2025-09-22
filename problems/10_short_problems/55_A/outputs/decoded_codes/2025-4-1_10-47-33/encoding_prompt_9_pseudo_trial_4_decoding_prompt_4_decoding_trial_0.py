def main():
    # Read the number of elements
    n = int(input())
    
    # Initialize the marked list with all elements set to True
    marked = [True] * n
    
    # Initialize current index and step size
    current_index = 0
    step_size = 1
    
    # Iterative marking process
    while step_size <= 500000:
        if marked[current_index]:
            marked[current_index] = False  # Mark the current position as False
        step_size += 1
        current_index = (current_index + step_size) % n  # Calculate the next position
    
    # Check remaining True values in the marked list
    remaining_true = [value for value in marked if value]
    
    # Output the result
    if len(remaining_true) == 0:
        print("YES")
    else:
        print("NO")

# Call the main function
main()
