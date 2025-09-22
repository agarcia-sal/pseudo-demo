def main_function():
    # Step 1: Read two lines of input
    first_set = input()
    second_set = input()
    
    # Step 2: Split the input lines into two lists of numbers
    first_list = first_set.split()
    second_list = second_set.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare corresponding elements from each list
    for index in range(3):  # loop from 0 to 2 inclusive
        # Convert the current elements to integers
        first_number = int(first_list[index])
        second_number = int(second_list[index])
        
        # Step 5: Check if the numbers are different
        if first_number != second_number:
            difference_count += 1  # Increment the counter
    
    # Step 6: Determine the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main section of the program
main_function()
