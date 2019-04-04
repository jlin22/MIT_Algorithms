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


if __name__ == "__main__":
    a = [random.randint(0, 10) for i in range(100000)]
    b = [0 for i in range(100000)]
    counting_sort(a, b, 1000)
    print(b)
