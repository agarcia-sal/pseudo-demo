val_map = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

def sort_numbers(nums):
    return ' '.join(sorted([x for x in nums.split(' ') if x], key=lambda x: val_map[x]))