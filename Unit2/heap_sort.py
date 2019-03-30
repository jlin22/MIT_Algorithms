def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def max_heapify(a, x):
    '''x is the index of the one violation of the heap property'''
    largest = x
    if left(x) <= heap_size(a) and a[left(x)] > a[largest]:
        largest = left(x)
    if right(x) <= heap_size(a) and  a[right(x)] > a[largest]:
        largest = right(x)
    if largest != x:
        swap(a, x, largest)
        max_heapify(a, largest)
    return a

def left(x):
    return 2*x

def right(x):
    return 2*x+1

def heap_size(a):
    return len(a)-1

def build_max_heap(a):
    for i in reversed(range(1, heap_size(a) // 2 + 1)):
        max_heapify(a, i)
    return a

def check_heap_invariant(a):
    return check_heap_node(a, 1)

def check_heap_node(a, x):
    if x > heap_size(a):
        return True
    else:
        left_check, right_check = True, True
        if left(x) < heap_size(a):
            left_check = a[left(x)] <= a[x]
        if right(x) < heap_size(a):
            right_check = a[right(x)] <= a[x]
        return left_check and right_check and check_heap_node(a, left(x)) and check_heap_node(a, right(x))

def extract_max(a):
    swap(a, 1, heap_size(a))
    max_key = a[heap_size(a)]
    a.pop()
    max_heapify(a, 1)
    return max_key

def heap_sort(a):
    s = []
    while not heap_empty(a):
        s.append(extract_max(a))
    return list(reversed(s))

def heap_empty(a):
    return heap_size(a) <= 0

if __name__ == "__main__":
    a = [15, 126, 124, 12, 3, 4, 6, 12, 33]
    print(build_max_heap(a))
    print(check_heap_invariant(a))
    print(heap_sort(a))
    
