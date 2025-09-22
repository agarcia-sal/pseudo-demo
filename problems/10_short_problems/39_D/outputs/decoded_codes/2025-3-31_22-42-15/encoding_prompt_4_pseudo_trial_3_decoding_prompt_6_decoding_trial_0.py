def main():
    # Read input values
    first_time = input()  # Taking the first time input
    second_time = input()  # Taking the second time input
    
    # Split the input strings into lists
    components1 = first_time.split()  # Splitting first time into components
    components2 = second_time.split()  # Splitting second time into components
    
    # Initialize a counter for differences
    difference_count = 0 
    
    # Compare corresponding components of both times
    for index in range(3):  # Looping from 0 to 2
        # Convert components to integers
        value1 = int(components1[index])  # Converting component to integer
        value2 = int(components2[index])  # Converting component to integer
        
        # Check if the values are different
        if value1 != value2:  # If the two values are not equal
            difference_count += 1  # Increment the count of differences
    
    # Determine result based on the number of differences
    if difference_count < 3:  # If differences are less than 3
        print("YES")  # Output "YES"
    else:
        print("NO")  # Output "NO"

# Start the main function when the script runs
main()  # Calling the main function
