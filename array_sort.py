unsorted_int = [14, 1, -1, 0, 7, 3, 21, 100, 10, 3, 5, 14, 11, 9, 8, -6]
unsorted_str = ['14', '1', '3', '10', '3', '5', '9', '8']

#With Sort
unsorted_int.sort()
print(unsorted_int)
unsorted_str.sort(key=int)
print(unsorted_str)

#With Sorted
print(sorted(unsorted_int))
print(sorted(unsorted_str, key=int, reverse=True)) #DESC
print(sorted(unsorted_str, key=int, reverse=False)) #ASC