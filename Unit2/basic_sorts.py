import time

def swap(a, p, q):
    temp = a[p]
    a[p] = a[q]
    a[q] = temp

def time_func(func):
    def modified_func(inputs):
        start = time.time()
        output = func(inputs)
        end = time.time()
        print(end - start)
        return output
    return modified_func

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

def binary_search(a, key, low, high):
    while low <= high:
        mid = (low + high) // 2
        if key < a[mid]:
            high = mid-1
        elif key > a[mid]:
            low = mid+1
        else:
            return mid
    return high

print(binary_search(a, 44, 0, len(a)))

def binary_insertion_sort(a):
    for i in range(1, len(a)):
        j = binary_search(a, a[i], 0, i-1)
        k = i-1
        while k > j:
            swap(a, k+1, k)
            k -= 1
    return a

a = [31, 64, 45, 28, 12, 50]
print(binary_insertion_sort(a))

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
#print(merge_sort(a))
print(binary_insertion_sort(a))
