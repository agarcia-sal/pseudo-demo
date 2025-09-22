def main():
    # Read two lines of input: first set and second set of values
    first_list = input()  # e.g. "1 2 3"
    second_list = input()  # e.g. "1 2 4"
    
    # Split the input strings into lists of values
    first_values = first_list.split()  # e.g. ['1', '2', '3']
    second_values = second_list.split()  # e.g. ['1', '2', '4']
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through each index from 0 to 2 (inclusive)
    for x in range(3):
        # Convert the x-th element of both lists to integers
        value_a = int(first_values[x])  # e.g. 1
        value_b = int(second_values[x])  # e.g. 1 or 4
        
        # Check if the values are different
        if value_a != value_b:
            # Increment the difference counter if they are not equal
            difference_count += 1
    
    # Determine the output based on the number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Call the main function when the script is executed
if __name__ == "__main__":
    main()
