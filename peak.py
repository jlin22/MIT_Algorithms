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

def fast_1dpeak_finder
