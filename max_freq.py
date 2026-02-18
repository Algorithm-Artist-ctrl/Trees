def most_frequent_number(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    max_count = 0
    result = None
    
    for num in arr:
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    
    return result
print(most_frequent_number([1,2,3,4,3,21,4]))