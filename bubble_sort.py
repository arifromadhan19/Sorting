unsorted_list = [14, 1, -1, 0, 7, 3, 21, 100, 10, 3, 5, 14, 11, 9, 8, -6]

#FOR VERSION
for passnum in range(len(unsorted_list) - 1, 0, -1):
#Loop from len(unsorted_list) until len(unsorted_list)=0
#with len(unsorted_list) -1 each loop
    for i in range(passnum):
        if unsorted_list[i] > unsorted_list[i + 1]:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[i + 1]
            unsorted_list[i + 1] = temp
print(unsorted_list)

#WHIILE VERSION
passnum = len(unsorted_list) -1
while passnum:
#loop passnum until passnum != None or passum != 0
    for i in range(passnum):
        if unsorted_list[i] > unsorted_list[i + 1]:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[i + 1]
            unsorted_list[i + 1] = temp
    passnum = passnum - 1
print(unsorted_list)
