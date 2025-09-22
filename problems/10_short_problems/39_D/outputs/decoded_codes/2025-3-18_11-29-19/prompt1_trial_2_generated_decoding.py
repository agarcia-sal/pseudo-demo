def main_procedure():
    # Read two lines of input
    first_input = input()
    second_input = input()
    
    # Split the input strings into lists of values
    first_list = first_input.split()
    second_list = second_input.split()
    
    # Initialize a counter to track the number of differences
    difference_count = 0 
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the current element from both lists to integers
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # Check if the two values are different
        if first_value != second_value:
            # Increment the difference counter
            difference_count += 1 
    
    # Check the count of differences
    if difference_count < 3:
        # Print "YES" if there are less than 3 differences
        print("YES")
    else:
        # Print "NO" if there are 3 or more differences
        print("NO")

# Main execution starts here
main_procedure()
