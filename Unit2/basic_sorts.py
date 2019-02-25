def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

a = [31, 64, 45, 28, 12, 50]
print(insertion_sort(a))
