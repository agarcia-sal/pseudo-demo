def do_main():
    # Read two lines of input representing two sets of values
    first_set = input()  # Read the first set of values
    second_set = input()  # Read the second set of values
    
    # Split each set into a list of values
    split_first = first_set.split()  # Split the first input into a list
    split_second = second_set.split()  # Split the second input into a list
    
    # Initialize a counter for differences
    differences_count = 0 
    
    # Loop through each corresponding pair of values in the two sets
    for index in range(3):  # Loop from index 0 to 2 (three iterations)
        # Convert the current value from each set to an integer
        value_from_first = int(split_first[index])  # Convert to integer
        value_from_second = int(split_second[index])  # Convert to integer
        
        # Check if the current pair of values are not equal
        if value_from_first != value_from_second:  # Check for inequality
            # Increment the differences count if they are not equal
            differences_count += 1  # Increment the counter
            
    # Determine if the number of differences is less than 3
    if differences_count < 3:  # Check if differences are less than 3
        print("YES")  # Output "YES" if less than 3 differences
    else:
        print("NO")  # Output "NO" otherwise

# The main program starts here
if __name__ == "__main__":
    do_main()  # Call the function to execute the main logic
