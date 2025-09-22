# Start Program

# Get Input:
input_value = abs(int(input()))

# Initialize Variables:
index = 0  # to keep track of the current number we are evaluating

# Repeat Until Condition Met:
while True:
    # Calculate sum_up_to_index
    sum_up_to_index = index * (index + 1) / 2
    
    # Calculate difference
    difference = sum_up_to_index - input_value
    
    # Check Conditions:
    if sum_up_to_index == input_value:
        print(index)  # print this index (this is the solution)
        break  # stop the program
        
    if sum_up_to_index > input_value:
        if difference % 2 == 0:  # check if difference is even
            print(index)  # print this index (this is the solution)
            break  # stop the program
            
    # Increment index by 1
    index += 1

# End Program
