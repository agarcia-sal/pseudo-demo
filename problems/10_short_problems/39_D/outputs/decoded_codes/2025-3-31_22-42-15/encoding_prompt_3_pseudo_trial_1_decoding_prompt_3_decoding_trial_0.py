def main():
    # Read two lines of input from the user
    first_set = input()
    second_set = input()
    
    # Split the input strings into lists of values
    first_values = first_set.split()
    second_values = second_set.split()
    
    # Initialize a counter to track differences
    difference_count = 0
    
    # Compare each corresponding value in the two lists
    for index in range(3):
        # Convert the string values to integers
        first_value = int(first_values[index])
        second_value = int(second_values[index])
        
        # Check if the values are different
        if first_value != second_value:
            difference_count += 1
            
    # Check the total number of differences
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")   # 3 or more differences

# The main block to run the function
if __name__ == "__main__":
    main()
