def find_number_matching_condition():
    user_input = abs(int(input()))
    index = 0
    
    while True:
        sum_value = (index * (index + 1)) // 2
        difference = sum_value - user_input
        
        if sum_value == user_input:
            print(index)
            break
        elif sum_value > user_input:
            if difference % 2 == 0:
                print(index)
                break
                
        index += 1
