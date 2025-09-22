def split_and_convert_to_integers(input_string):
    # Split the input string by spaces and convert each element to integer
    return [int(num) for num in input_string.split()]

def main():
    # Read two input strings
    input1 = input()
    input2 = input()
    
    # Split the input strings into lists of integers
    numbers1 = split_and_convert_to_integers(input1)
    numbers2 = split_and_convert_to_integers(input2)
    
    # Initialize a variable to count differences
    difference_count = 0 

    # Compare the first three integers from both lists
    for position in range(3):
        value1 = numbers1[position]
        value2 = numbers2[position]
        
        # If the integers are different, increment the difference counter
        if value1 != value2:
            difference_count += 1
            
    # Determine output based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# The following lines below are for testing and should typically be outside of main execution in actual code.
# Uncomment the lines below to test the function.
# main() 
# Example inputs for testing could include:
# input1 = "1 2 3"
# input2 = "1 2 4"  # Expected output: "YES"
