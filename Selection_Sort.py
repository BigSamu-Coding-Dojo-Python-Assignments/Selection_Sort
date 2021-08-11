import time

a = [2,3,5,6,8,1,4,7]
b = [6,3,7,4,8,2,5,1]
c = [8,2,5,7,1,6,4,3]

def selection_sort(someList):
    start_time = time.time()
    for j in range(len(someList)):
        minimum = someList[j]
        min_index = j
        for i in range(j,len(someList),1):
            if minimum>someList[i]:
                minimum=someList[i]
                min_index=i
        someList[j],someList[min_index] = someList[min_index],someList[j] 
    end_time = time.time()
    print(end_time-start_time)
    return someList

print(selection_sort(a))
print(selection_sort(b))
print(selection_sort(c))