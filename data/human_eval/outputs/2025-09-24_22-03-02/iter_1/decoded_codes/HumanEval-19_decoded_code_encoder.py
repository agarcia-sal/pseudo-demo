def sort_numbers(numbers):
    map = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    split_nums = numbers.split(' ')
    filtered = [x for x in split_nums if x != '']
    sorted_nums = sorted(filtered, key=lambda x: map[x])
    return ' '.join(sorted_nums)