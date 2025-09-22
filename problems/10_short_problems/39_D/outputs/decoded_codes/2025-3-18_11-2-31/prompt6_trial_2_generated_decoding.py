def main():
    # Read two input strings from the user
    first_string = input()
    second_string = input()
    
    # Split the input strings into lists of elements
    first_list = first_string.split()
    second_list = second_string.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Assuming both lists have at least 3 elements
        # Convert the elements to integers for comparison
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1
            
    # Determine the result based on the number of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
