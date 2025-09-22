def check_differences():
    # Prompt the user to enter the first set of integers
    print("Enter the first set of three integers separated by spaces:")
    first_set = input()  # Get the first set of integers as a string
    
    # Prompt the user to enter the second set of integers
    print("Enter the second set of three integers separated by spaces:")
    second_set = input()  # Get the second set of integers as a string
    
    # Split the input strings into separate integer values
    first_array = first_set.split()  # Split the first set into a list
    second_array = second_set.split()  # Split the second set into a list
    
    # Initialize a counter to track the number of differences
    difference_count = 0 
    
    # Loop through each index from 0 to 2 (for the three integers)
    for index in range(3):
        # Convert the strings at the current index to integers
        first_value = int(first_array[index])  # Convert first value to integer
        second_value = int(second_array[index])  # Convert second value to integer
        
        # Check if the two values differ
        if first_value != second_value:
            difference_count += 1  # Increment the count of differences

    # After comparing all integers, check the number of differences
    if difference_count < 3:
        print("YES")  # Output "YES" if there are fewer than 3 differences
    else:
        print("NO")   # Output "NO" if there are 3 or more differences

# Call the function to execute the comparisons
check_differences()
