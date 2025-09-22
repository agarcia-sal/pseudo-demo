def main():
    # Read two lines of input from the user
    first_line = input()
    second_line = input()
    
    # Split the input lines into separate values
    first_values = first_line.split()
    second_values = second_line.split()
    
    # Initialize a variable to count differences
    difference_count = 0 
    
    # Compare corresponding values from both lists
    for index in range(3):
        first_value = int(first_values[index])  # Convert first value to integer
        second_value = int(second_values[index])  # Convert second value to integer
        
        # Check for inequality between the two values
        if first_value != second_value:
            difference_count += 1  # Increase count if values are not equal
            
    # Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")  # Output "YES" if differences are less than 3
    else:
        print("NO")   # Output "NO" if differences are 3 or more

# Start the main function
main()
