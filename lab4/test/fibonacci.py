from timeit import timeit
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

cache = {}

def fibonacchi_alt(idx):  #nhanh hon 1 nhung ko tinh dc nhieu
    if idx in cache:
        return cache[idx]

    if idx <= 1:
        return idx

    res = fibonacchi_alt(idx-1) + fibonacchi_alt(idx-2)
    cache[idx] = res
    return res

def fibonacci_iterative(n):   # cham hon 2 nhung tinh dc nhieu
    cache = [0]*(n+1)
    cache[1] = 1
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

if __name__ == "__main__":
    while True:
        n = int(input("nhap n: "))

        # res = timeit("fibonacci(n)", number=1, globals=globals())
        # print(res)

        res_cached = timeit("fibonacchi_alt(n)", number=1, globals=globals())
        print(res_cached)

        res_iterative = timeit("fibonacci_iterative(n)", number=1, globals=globals())
        print(res_iterative)
