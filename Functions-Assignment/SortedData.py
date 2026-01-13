# Write a function that returns sorted data.

def sortedData(lst):
    sortedList = []
    for i in range(len(lst)):
        m = lst[i]
        n = 0
        for j in range(i+1, len(lst)):
            if m > lst[j]:
                m = lst[j]
                n = j
        lst[n] = lst[i]
        sortedList.append(m)
    
    print(sortedList)

lst = []
sortedData(lst)