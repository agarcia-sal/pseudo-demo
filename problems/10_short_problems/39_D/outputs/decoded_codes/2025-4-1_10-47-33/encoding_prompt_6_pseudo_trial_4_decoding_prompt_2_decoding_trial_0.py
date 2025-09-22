def main():
    # Read two lines of input representing two sets of values
    first_set = input()
    second_set = input()
    
    # Split the input lines into lists for comparison
    first_values = first_set.split()
    second_values = second_set.split()
    
    # Initialize a variable to count the number of differences
    differences_count = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # index goes from 0 to 2
        # Convert the current elements from strings to integers for comparison
        value_from_first_set = int(first_values[index])
        value_from_second_set = int(second_values[index])
        
        # If the values from the two sets are different, increment the count
        if value_from_first_set != value_from_second_set:
            differences_count += 1
    
    # Check the total number of differences and print the result
    if differences_count < 3:
        print("YES")
    else:
        print("NO")

# Execute the main function
main()
