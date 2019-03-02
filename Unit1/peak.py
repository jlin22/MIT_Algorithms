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


