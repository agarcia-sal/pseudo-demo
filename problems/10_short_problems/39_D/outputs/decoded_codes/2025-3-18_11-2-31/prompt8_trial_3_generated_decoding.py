def main():
    # Get input from the user
    first_input = input()
    second_input = input()
    
    # Split the inputs into lists of strings
    list1 = first_input.split()
    list2 = second_input.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        first_number = int(list1[index])
        second_number = int(list2[index])
        
        # Check if the numbers are not equal
        if first_number != second_number:
            # Increment the difference count
            difference_count += 1
    
    # Determine if the count of differences is less than 3
    if difference_count < 3:
        print("YES")  # There are less than 3 differences
    else:
        print("NO")   # There are 3 or more differences

# Start the program by calling the main function
main()
