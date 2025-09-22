def doMain():
    # Read two lines of input representing two sets of values
    FIRST_SET = input()
    SECOND_SET = input()
    
    # Split each set into a list of values
    SPLIT_FIRST = FIRST_SET.split()
    SPLIT_SECOND = SECOND_SET.split()
    
    # Initialize a counter for differences
    differences_count = 0 
    
    # Loop through each corresponding pair of values in the two sets
    for index in range(3):
        # Convert the current value from each set to an integer
        value_from_first = int(SPLIT_FIRST[index])
        value_from_second = int(SPLIT_SECOND[index])
        
        # Check if the current pair of values are not equal
        if value_from_first != value_from_second:
            # Increment the differences count if they are not equal
            differences_count += 1 
    
    # Determine if the number of differences is less than 3
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# The main program starts here
if __name__ == "__main__":
    doMain()
