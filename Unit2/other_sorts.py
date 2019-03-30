import random

def swap(a, i, j):
    a[i], a[j] = a[j], a[i]
    return a

def bubble_sort(a):
    for i in range(1, len(a)):
        inversions = 0
        for j in reversed(range(i, len(a))):
            if a[j-1] > a[j]:
                swap(a, j-1, j)
                inversions += 1
        if not inversions:
            break
    return a

def selection_sort(a):
    for i in range(0, len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        swap(a, min_index, i)
    return a

def shuffle(a):
    for i in range(1, len(a)):
        r = int(random.randint(0, i))
        swap(a, i, r)
    return a
        
if __name__ == "__main__":
    a = [1, 5, 6, 7]
    a = swap(a, 1, 2)
    print(a)
    print(bubble_sort(a))
    b = [100, 65, 45, 33, 22, 11, 9, 8, 7]
    print(bubble_sort(b))
    print("shuffled", shuffle(b))
    print(selection_sort(b))
    
