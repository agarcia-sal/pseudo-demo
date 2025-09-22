def main():
    # Receive input from the user for the first set of integers
    first_input = input()
    # Receive input from the user for the second set of integers
    second_input = input()
    
    # Split the input strings into lists of integers
    first_set = list(map(int, first_input.split()))
    second_set = list(map(int, second_input.split()))

    # Initialize a counter to track differences
    difference_count = 0

    # Compare the corresponding items from both sets
    for index in range(3):  # Loop through indices 0, 1, and 2
        first_number = first_set[index]  # Get number from the first set
        second_number = second_set[index]  # Get number from the second set
        
        # Check if the numbers are different
        if first_number != second_number:
            difference_count += 1  # Increment the difference counter

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# Execute the main function
main()
