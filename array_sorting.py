unsorted_list = [14, 1, -1, 0, 7, 3, 21, 100, 10, 3, 5, 14, 11, 9, 8, -6]

sorted_list = []
while unsorted_list:
    min_unsorted_list = min(unsorted_list)
    for x in unsorted_list:
        if x < min_unsorted_list:
            min_unsorted_list = x
    sorted_list.append(min_unsorted_list)
    unsorted_list.remove(min_unsorted_list)
print(sorted_list)
