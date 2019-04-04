import random

def counting_sort(a, b, k, key=(lambda x: x)):
    c = [0 for i in range(k+1)]
    for element in a:
        c[key(element)] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for element in reversed(a):
        b[c[key(element)]-1] = element
        c[key(element)] -= 1

def dth_digit_function(d):
    return lambda x: (x // (10 ** d)) % 10

def radix_sort(a, d):
    b = [0 for i in range(len(a))]
    for i in range(d):
        counting_sort(a, b, 10, dth_digit_function(i))
    return b

def sorted(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

def is_permutation(a, b):
    count = {}
    for item in a:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
    for item in b:
        if item not in count:
            return False
        else:
            count[item] -= 1
            if count[item] < 0:
                return False
    for value in count.values():
        if value != 0:
            return False
    return True
        
if __name__ == "__main__":
    a = [random.randint(0, 10) for i in range(100000)]
    b = [0 for i in range(100000)]
    counting_sort(a, b, 1000)
    print(b)
    print("sorted", sorted(b))
    print("is_permutation(a, b)", is_permutation(a, b))
