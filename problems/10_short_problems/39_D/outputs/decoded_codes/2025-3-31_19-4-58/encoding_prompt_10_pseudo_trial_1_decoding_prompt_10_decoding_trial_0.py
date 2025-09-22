def main():
    # Read input from user
    t1 = input()
    t2 = input()
    
    # Split the input strings into lists of strings
    numbers_t1 = t1.split()  # splits t1 into a list of strings
    numbers_t2 = t2.split()  # splits t2 into a list of strings
    
    # Initialize count of differing integers
    difference_count = 0
    
    # Loop through the first three elements and count differences
    for i in range(3):
        a = int(numbers_t1[i])  # Convert string to integer
        b = int(numbers_t2[i])  # Convert string to integer
        
        # Check if the values are different
        if a != b:
            difference_count += 1  # Increment the difference counter
    
    # Decide based on the count of differences
    if difference_count < 3:
        print("YES")  # Less than three differences
    else:
        print("NO")   # Three or more differences

# Main program execution
main()
