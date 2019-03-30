def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a

def bubble_sort(a):
    for i in range(1, len(a)):
        for j in reversed(range(i, len(a))):
            if a[j-1] > a[j]:
                swap(a, j-1, j)
    return a

if __name__ == "__main__":
    a = [1, 5, 6, 7]
    a = swap(a, 1, 2)
    print(a)
    print(bubble_sort(a))
    b = [100, 65, 45, 33, 22, 11, 9, 8, 7]
    print(bubble_sort(b))
    
