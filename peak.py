def linear_1dpeak_finder(a):
    for i in range(len(a)):
        if i == 0:
            if a[i] > a[i+1]:
                return i
        elif i == len(a) - 1:
            if a[i] > a[i-1]:
                return i
        else:
            if a[i] > a[i-1] and a[i] > a[i+1]:
                return i

a = [2, 4, 6, 4]
print("the peak is at " + str(linear_1dpeak_finder(a)))

def fast_1dpeak_finder(a):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            if a[mid] > a[mid+1]:
                return mid
            else:
                high = high // 2 
        elif mid == len(a) - 1:
            if a[mid] > a[mid-1]:
                return mid
        else:
            if a[mid+1] > a[mid]:
                low = mid+1
            elif a[mid-1] > a[mid]:
                high = mid-1
            else:
                return mid

print("the peak is at " + str(fast_1dpeak_finder(a)))

def greedy_ascent(a):
    pass

def fast_2dpeak_finder(a):
    pass
        

