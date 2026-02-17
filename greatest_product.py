def greatest_product_equal_to_element(arr):
    s = set(arr)
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    arr_sorted = sorted(arr, reverse=True)
    for target in arr_sorted:
        for a in s:
            if a == 0:
                if target == 0 and freq.get(0, 0) > 1:
                    return 0
                continue
            if target % a == 0:
                b = target // a
                if b in s:
                    if a != b or freq[a] > 1:
                        if a * b == target:
                            return target
    return -1
a=[12,13,14,12,2]
print(greatest_product_equal_to_element(a))