def main():
    # Read two sets of input
    first_string = input()
    second_string = input()
    
    # Split the input strings into lists
    first_list = first_string.split()
    second_list = second_string.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert current list elements to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the corresponding values are different
        if first_value != second_value:
            # Increment differenceCount by 1 
            difference_count += 1 
    
    # Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
