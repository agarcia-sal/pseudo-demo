def main():
    # Read two lines of input
    first_line = input()
    second_line = input()
    
    # Split the input lines into lists of strings
    list1 = first_line.split()
    list2 = second_line.split()
    
    # Initialize a counter for differences
    difference_count = 0
    
    # Loop through the index range of the first three elements
    for index in range(3):
        # Convert the current elements to integers
        value_from_first_line = int(list1[index])
        value_from_second_line = int(list2[index])
        
        # Compare the corresponding values
        if value_from_first_line != value_from_second_line:
            # Increment the difference counter
            difference_count += 1
            
    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")  # Fewer than 3 differences
    else:
        print("NO")   # 3 or more differences

# Execute the main function if this module is run directly
if __name__ == "__main__":
    main()


1 2 3
1 2 4
