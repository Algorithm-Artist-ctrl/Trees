#Hasing Problem
def countOddEven(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    odd_count = 0
    even_count = 0

    for key in freq:
        if freq[key] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count

arr = [1, 2, 2, 3, 3, 3, 4, 4]
print(countOddEven(arr))
