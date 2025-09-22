def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split each line into a list of strings
    first_list = first_line.split()
    second_list = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the string elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values at the current index are different
        if first_value != second_value:
            difference_count += 1
            
    # Check the total count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
