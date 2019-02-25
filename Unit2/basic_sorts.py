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

def merge_sort(a):
    return merge_sort_helper(a, 0, len(a)-1)

def merge_sort_helper(a, p, q):
    if p < q:
        mid = (p + q) // 2
        merge_sort_helper(a, p, mid)
        merge_sort_helper(a, mid+1, q)
        merge(a, p, mid, q)
    return a

def merge(a, p, r, q):
    left = a[p:r+1]
    right = a[r+1:q+1]
    i, j = 0, 0
    k = p
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    return a

a = [31, 64, 45, 28, 12, 50]
print(merge_sort(a))
