def linear_peakfinder(a):
    # Return index of peak, -1 if there is no peak
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
    # Never reaches this point
    return -1

def fast_peakfinder(a):
    # Uses binary search to look for a peak
    return fast_pf_helper(a, 0, len(a) - 1)

def fast_pf_helper(a, start, end):
    # Never reaches this point
    if start > end:
        return -1
    mid = (start + end) // 2
    if in_boundary(mid-1, start, end) and a[mid - 1] >= a[mid]:
        return fast_pf_helper(a, start, mid-1)
    elif in_boundary(mid+1, start, end) and a[mid + 1] >= a[mid]:
        return fast_pf_helper(a, mid+1, end)
    else:
        return mid
    
def in_boundary(ind, start, end):
    return ind >= start and ind <= end

# For both matrix peak finders, assume that the 2d array is square

def greedy_ascent(a):
    i, j = start(a)
    traversed = {}
    while (i, j) not in traversed:
        n = find_best_neighbor(a, i, j)
        if n == (i, j):
            return n
        traversed[(i, j)] = 1
        i, j = n
    return -1

def start(a):
    return 0, 0

def find_best_neighbor(a, p, q):
    n, m = len(a), len(a[0])
    largest = (p, q)
    if p-1 >= 0 and a[p-1][q] > a[largest[0]][largest[1]]:
        largest = (p-1, q)
    if q-1 >= 0 and a[p][q-1] > a[largest[0]][largest[1]]:
        largest = (p, q-1)
    if p+1 < n and a[p+1][q] > a[largest[0]][largest[1]]:
        largest = (p+1, q)
    if q+1 < m and a[p][q+1] > a[largest[0]][largest[1]]:
        largest = (p, q+1)
    return largest

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(fast_peakfinder(a))
    print(linear_peakfinder(a))
    a = [[0, 0, 0, 0],
         [1, 0, 0, 0],
         [2, 3, 4, 5],
         [0, 0, 0, 0],]
    print(greedy_ascent(a))

    
