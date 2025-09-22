def main():
    # Step 1: Read input values
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Step 3: Initialize a difference counter
    difference_counter = 0
    
    # Step 4: Compare corresponding elements in the two lists
    for index in range(3):  # Loop through the first three elements
        value_a = int(first_list[index])
        value_b = int(second_list[index])
        
        # If the values are different, increment the difference counter
        if value_a != value_b:
            difference_counter += 1
    
    # Step 5: Determine if the number of differences is less than 3
    if difference_counter < 3:
        print("YES")  # There are fewer than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Execute the main function
main()
