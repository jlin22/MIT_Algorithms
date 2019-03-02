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
    return fast_pf_helper(a, 0, len(a) - 1)

def fast_pf_helper(a, start, end):
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

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(fast_peakfinder(a))
    
