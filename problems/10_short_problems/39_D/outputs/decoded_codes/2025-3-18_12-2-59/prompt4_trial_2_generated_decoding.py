def main():
    # Read input strings
    first_string = input()
    second_string = input()
    
    # Split the input strings into lists of strings
    first_list = first_string.split()
    second_list = second_string.split()
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert each element to an integer
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        # If the values are not equal, increment the difference counter
        if first_value != second_value:
            difference_count += 1 

    # Determine if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Start execution
main()
