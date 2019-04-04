import random

def counting_sort(a, b, k):
    c = [0 for i in range(k+1)]
    for key in a:
        c[key] += 1
    for i in range(1, k+1):
        c[i] += c[i-1]
    for key in reversed(a):
        b[c[key]-1] = key
        c[key] -= 1

if __name__ == "__main__":
    a = [random.randint(0, 10) for i in range(100000)]
    b = [0 for i in range(100000)]
    counting_sort(a, b, 1000)
    print(b)
