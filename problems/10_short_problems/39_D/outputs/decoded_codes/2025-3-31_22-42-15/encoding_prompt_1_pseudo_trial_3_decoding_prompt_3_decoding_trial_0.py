def do_main():
    # Read two lines of input from the user
    first_set = input()
    second_set = input()
    
    # Split each set of values into a list
    split_first = first_set.split()
    split_second = second_set.split()
    
    # Initialize a counter for differences
    differences_count = 0 
    
    # Loop through the first three indices of each list
    for index in range(3):
        # Convert the current value from each set to an integer
        value_from_first = int(split_first[index])
        value_from_second = int(split_second[index])
        
        # Increment the differences count if the values are not equal
        if value_from_first != value_from_second:
            differences_count += 1 
    
    # Determine if the number of differences is less than 3
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# The main program starts here
if __name__ == "__main__":
    do_main()
