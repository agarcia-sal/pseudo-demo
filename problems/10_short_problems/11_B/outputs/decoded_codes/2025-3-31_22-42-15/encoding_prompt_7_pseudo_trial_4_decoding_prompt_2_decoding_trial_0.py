def find_integer_with_specific_property():
    input_value = int(input())
    absolute_value = abs(input_value)
    index = 0
    
    while True:
        sum_of_first_index = (index * (index + 1)) // 2  # Using integer division
        difference = sum_of_first_index - absolute_value
        
        if sum_of_first_index == absolute_value:
            print(index)
            break
        elif sum_of_first_index > absolute_value:
            if difference % 2 == 0:
                print(index)
                break
        
        index += 1  # Increment index by 1
