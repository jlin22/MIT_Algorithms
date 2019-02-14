def linear_1dpeak_finder(a):
    for i in range(len(a)):
        if i == 0:
            if a[i] >= a[i+1]:
                return i
        elif i == len(a) - 1:
            if a[i] >= a[i-1]:
                return i
        else:
            if a[i] >= a[i-1] and a[i] >= a[i+1]:
                return i
    return -1

a = [2, 4, 6, 4]
print("the peak is at " + str(linear_1dpeak_finder(a)))

def fast_1dpeak_finder(a):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            if a[mid] >= a[mid+1]:
                return mid
            else:
                high = high // 2 
        elif mid == len(a) - 1:
            if a[mid] >= a[mid-1]:
                return mid
        else:
            if a[mid+1] > a[mid]:
                low = mid+1
            elif a[mid-1] > a[mid]:
                high = mid-1
            else:
                return mid
    return -1

print("the peak is at " + str(fast_1dpeak_finder(a)))

def greedy_ascent(a):
    i, j = 0, 0
    n, m = len(a), len(a[0])
    while True:
        if i+1 < n and a[i][j] < a[i+1][j]:
            i = i+1
        elif j+1 < m and a[i][j] < a[i][j+1]:
            j = j+1
        elif i-1 >= 0 and a[i][j] < a[i-1][j]:
            i = i-1
        elif j-1 >= 0 and a[i][j] < a[i][j-1]:
            j = j-1
        else:
            return [i, j]
    return -1

def fast_2dpeak_finder(a):
    n, m = len(a), len(a[0])
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        peak1d = fast_1dpeak_finder(a[mid])
        if a[mid][peak1d] < a[mid-1][peak1d]:
            high = mid-1
        elif a[mid][peak1d] < a[mid+1][peak1d]:
            low = mid+1
        else:
            return [mid, peak1d]
    return -1


    
        
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
print(greedy_ascent(a))

print(fast_2dpeak_finder(a))

